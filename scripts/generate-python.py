#!/usr/bin/env python3
"""Normalize the shared OpenAPI source and generate Python endpoint bindings."""

from __future__ import annotations

import copy
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "openapi" / "openapi.yaml"
OUTPUT = ROOT / "python" / "trustify_client" / "generated"
CONFIG = ROOT / "python" / "generator-config.yml"


def normalize_document(document: dict[str, Any]) -> dict[str, Any]:
    """Adapt known OpenAPI 3.1 and Trustify wire-format constructs."""
    document = copy.deepcopy(document)
    version = document.get("openapi", "")
    if not version.startswith("3.1."):
        raise ValueError(f"expected OpenAPI 3.1, found {version!r}")

    _normalize_value(document)
    document["openapi"] = "3.0.3"
    document.get("info", {}).get("license", {}).pop("identifier", None)

    for path, path_item in document.get("paths", {}).items():
        placeholders = set(re.findall(r"\{([^{}]+)\}", path))
        parameters = path_item.get("parameters", [])
        _normalize_parameters(parameters, placeholders, upload_sbom=False)
        for method, operation in path_item.items():
            if method.lower() not in {
                "get",
                "put",
                "post",
                "delete",
                "patch",
                "head",
                "options",
            }:
                continue
            _normalize_parameters(
                operation.get("parameters", []),
                placeholders,
                upload_sbom=operation.get("operationId") == "uploadSbom",
            )

    schemas = document.get("components", {}).get("schemas", {})
    requested_scores = schemas.get("RequestedField_Vec_Vec_ScoredVector", {})
    items = requested_scores.get("items")
    if requested_scores.get("type") == "array" and isinstance(items, dict):
        requested_scores["items"] = {"$ref": "#/components/schemas/ScoredVector"}

    return document


def _normalize_value(value: Any) -> None:
    if isinstance(value, list):
        for item in value:
            _normalize_value(item)
        return
    if not isinstance(value, dict):
        return

    for item in value.values():
        _normalize_value(item)

    content = value.get("content")
    if isinstance(content, dict):
        _normalize_content(content)

    types = value.get("type")
    if isinstance(types, list) and "null" in types:
        concrete_types = [item for item in types if item != "null"]
        if len(concrete_types) != 1:
            raise ValueError(f"unsupported nullable type union: {types!r}")
        value["type"] = concrete_types[0]
        value["nullable"] = True

    for union_name in ("oneOf", "anyOf"):
        branches = value.get(union_name)
        if not isinstance(branches, list):
            continue
        null_branches = [branch for branch in branches if branch.get("type") == "null"]
        if not null_branches:
            continue
        if len(null_branches) != 1:
            raise ValueError(
                f"unsupported nullable {union_name} with multiple null branches"
            )
        concrete = [branch for branch in branches if branch.get("type") != "null"]
        del value[union_name]
        if len(concrete) == 1:
            branch = concrete[0]
            if "$ref" in branch:
                if "description" in branch:
                    value.setdefault("description", branch["description"])
                branch = {
                    key: item for key, item in branch.items() if key != "description"
                }
                value["allOf"] = [branch]
            else:
                for key, item in branch.items():
                    value.setdefault(key, item)
        else:
            value["allOf"] = [{union_name: concrete}]
        value["nullable"] = True

    if value.get("in") == "header" and isinstance(value.get("schema"), dict):
        value["schema"].pop("nullable", None)


def _normalize_content(content: dict[str, Any]) -> None:
    for old_type, new_type in (
        ("application/merge-patch+json", "application/json"),
        ("text/plain", "application/octet-stream"),
        ("application/gzip", "application/octet-stream"),
    ):
        if old_type not in content:
            continue
        if new_type in content:
            raise ValueError(
                f"cannot normalize duplicate content types {old_type} and {new_type}"
            )
        media = content.pop(old_type)
        content[new_type] = media
        if old_type in {"text/plain", "application/gzip"}:
            _set_binary_schema(media.get("schema"))

    binary = content.get("application/octet-stream", {})
    schema = binary.get("schema") if isinstance(binary, dict) else None
    if isinstance(schema, dict) and schema.get("type") == "array":
        items = schema.get("items", {})
        if isinstance(items, dict) and items.get("type") == "integer":
            _set_binary_schema(schema)


def _set_binary_schema(schema: Any) -> None:
    if not isinstance(schema, dict):
        return
    schema.pop("items", None)
    schema["type"] = "string"
    schema["format"] = "binary"


def _normalize_parameters(
    parameters: list[dict[str, Any]], placeholders: set[str], upload_sbom: bool
) -> None:
    for parameter in parameters:
        if parameter.get("in") == "path" and parameter.get("name") not in placeholders:
            parameter["in"] = "query"
        if upload_sbom and parameter.get("in") == "query":
            parameter["required"] = False


def main() -> None:
    document = yaml.safe_load(SPEC.read_text(encoding="utf-8"))
    normalized = normalize_document(document)

    generator = shutil.which("openapi-python-client")
    if generator is None:
        candidate = Path(sys.executable).with_name("openapi-python-client")
        generator = str(candidate) if candidate.is_file() else None
    if generator is None:
        raise SystemExit(
            "openapi-python-client is required; run scripts/generate-python.sh"
        )

    with tempfile.TemporaryDirectory(prefix="trustify-openapi-") as temporary:
        normalized_spec = Path(temporary) / "openapi.yaml"
        normalized_spec.write_text(
            yaml.safe_dump(normalized, sort_keys=False), encoding="utf-8"
        )
        result = subprocess.run(
            [
                generator,
                "generate",
                "--path",
                str(normalized_spec),
                "--output-path",
                str(OUTPUT),
                "--config",
                str(CONFIG),
                "--meta",
                "none",
                "--overwrite",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        sys.stdout.write(result.stdout)
        sys.stderr.write(result.stderr)
        if result.returncode:
            raise subprocess.CalledProcessError(result.returncode, result.args)
        if any(
            marker in result.stdout or marker in result.stderr
            for marker in (
                "Warning(s) encountered",
                "WARNING parsing",
                "Unable to parse schema",
                "Unable to process schema",
            )
        ):
            raise SystemExit(
                "Python API generation reported omitted endpoints or models"
            )


if __name__ == "__main__":
    main()
