import os

from trustify_client import TrustifyClient
from trustify_client.generated.api.default import info


def main() -> None:
    base_url = os.getenv("TRUSTIFY_URL", "http://localhost:8080")
    with TrustifyClient(
        base_url,
        bearer_token=os.getenv("TRUSTIFY_TOKEN") or None,
        raise_on_unexpected_status=True,
    ) as client:
        result = info.sync(client=client.api)

    if result is None:
        raise RuntimeError("Trustify server returned no info response")

    print(f"Server: {base_url}")
    print(f"Version: {result.version}")
    print(f"Read only: {result.read_only}")
    print(f"Exploit intelligence: {result.exploit_intelligence}")


if __name__ == "__main__":
    main()
