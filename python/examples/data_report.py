import argparse
import os
from collections import Counter

from trustify_client import TrustifyClient
from trustify_client.generated.api.sbom import list_sboms
from trustify_client.generated.api.vulnerability import list_vulnerabilities
from trustify_client.generated.models.base_score import BaseScore
from trustify_client.generated.types import Unset


def total_or_unknown(total: int | None | Unset) -> str:
    if total is None or isinstance(total, Unset):
        return "unknown"
    return f"{total:,}"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Summarize SBOM and vulnerability data from Trustify"
    )
    parser.add_argument(
        "--limit", type=int, default=100, help="records to inspect from each endpoint"
    )
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit must be greater than zero")

    base_url = os.getenv("TRUSTIFY_URL", "http://localhost:8080")
    with TrustifyClient(
        base_url,
        bearer_token=os.getenv("TRUSTIFY_TOKEN") or None,
        raise_on_unexpected_status=True,
    ) as client:
        sboms = list_sboms.sync(
            client=client.api,
            sort="ingested:desc",
            limit=args.limit,
            total=True,
        )
        vulnerabilities = list_vulnerabilities.sync(
            client=client.api,
            sort="published:desc",
            limit=args.limit,
            total=True,
        )

    if sboms is None or vulnerabilities is None:
        raise RuntimeError("Trustify server returned an empty report response")

    severities = Counter(
        item.base_score.severity.value
        if isinstance(item.base_score, BaseScore)
        else "unknown"
        for item in vulnerabilities.items
    )

    print(f"Trustify data report: {base_url}")
    print(f"SBOMs: {total_or_unknown(sboms.total)} total; sampled {len(sboms.items)}")
    print(
        "Vulnerabilities: "
        f"{total_or_unknown(vulnerabilities.total)} total; "
        f"sampled {len(vulnerabilities.items)}"
    )
    print("Severity in sampled vulnerabilities:")
    for severity, count in sorted(severities.items()):
        print(f"  {severity}: {count}")


if __name__ == "__main__":
    main()
