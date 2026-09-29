import argparse
import os

from trustify_client import TrustifyClient
from trustify_client.generated.api.sbom import list_sboms
from trustify_client.generated.types import Unset


def main() -> None:
    parser = argparse.ArgumentParser(description="List recent SBOMs in Trustify")
    parser.add_argument("--limit", type=int, default=20, help="number of SBOMs to show")
    parser.add_argument("--query", help="optional Trustify SBOM search query")
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit must be greater than zero")

    base_url = os.getenv("TRUSTIFY_URL", "http://localhost:8080")
    with TrustifyClient(
        base_url,
        bearer_token=os.getenv("TRUSTIFY_TOKEN") or None,
        raise_on_unexpected_status=True,
    ) as client:
        page = list_sboms.sync(
            client=client.api,
            q=args.query,
            sort="ingested:desc",
            limit=args.limit,
            total=True,
        )

    if page is None:
        raise RuntimeError("Trustify server returned no SBOM list")

    total = (
        "unknown" if page.total is None or isinstance(page.total, Unset) else page.total
    )
    print(f"SBOMs on {base_url}: {total} total; showing {len(page.items)}")
    for sbom in page.items:
        print(
            f"{sbom.ingested.isoformat()}  {sbom.number_of_packages:>7} packages  "
            f"{sbom.name}  [{sbom.id}]"
        )


if __name__ == "__main__":
    main()
