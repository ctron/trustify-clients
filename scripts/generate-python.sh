#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
uv run --project "$repo_root/python" --group generate \
    python "$repo_root/scripts/generate-python.py"
