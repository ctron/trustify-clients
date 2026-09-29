# trustify-client

Python bindings for the Trustify REST API. The low-level sync and async
endpoint functions and models in `trustify_client.generated` are generated
from the pinned OpenAPI document in `../openapi/`. `TrustifyClient` provides
shared authentication, timeout, retry, and wire-format configuration.

## Install

From a checkout:

```sh
pip install ./python
```

## Quick start

```python
from trustify_client import TrustifyClient
from trustify_client.generated.api.default import info

with TrustifyClient("https://trustify.example", bearer_token="access-token") as client:
    info_response = info.sync(client=client.api)
    print(info_response)
```

Use `.asyncio` with the same generated operation for asynchronous requests:

```python
async with TrustifyClient("https://trustify.example") as client:
    info_response = await info.asyncio(client=client.api)
```

The `api` property is the low-level generated client. Generated `.sync` and
`.asyncio` calls return the parsed model; `.sync_detailed` and
`.asyncio_detailed` return a response object with the model in `.parsed`.
`raise_on_unexpected_status=True` can be set when constructing `TrustifyClient`
to raise on undocumented status codes. The client is a sync and async context
manager that closes the underlying HTTPX connection pools.

## Configuration

Requests are anonymous by default. Supply `bearer_token` for a fixed token,
or `token_provider` for a callback queried for each request. Async operations
also accept an async token provider. The provider returns the raw token without
the `Bearer` prefix. Applications own OIDC login, refresh, and token storage.

Connection and request timeouts default to 15 and 120 seconds. Retries are
disabled by default; `RetryPolicy.for_idempotent_requests(2)` retries GET and
HEAD connection/time-out failures and HTTP 429, 502, 503, and 504 responses
with bounded exponential backoff. Numeric `Retry-After` values are honored up
to the configured cap.

HTTPX automatically decompresses gzip and deflate; the package enables its
Brotli and Zstandard extras as well.

Pass TLS settings with `verify_ssl` and other HTTPX options such as `proxy`
through `httpx_args`.

Importer merge-patch and plain-text request content types are restored
automatically. Generated plain-text importer operations accept `File` bodies,
for example `File(payload=BytesIO(b"true"))`.

`collect_offset_pages` and `collect_offset_pages_async` collect offset-based
results using the reported total when available, or the first short/empty page
when it is not.

## Regenerate

The checked-in endpoints are generated from the shared OpenAPI source:

```sh
scripts/generate-python.sh
```

The generator uses `openapi-python-client` 0.29.1. A small normalization pass
adapts known OpenAPI 3.1 constructs and Trustify wire formats to the generator;
the canonical OpenAPI document is not modified.
