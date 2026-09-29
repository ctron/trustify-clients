# Python examples

These scripts call a live Trustify server. From the repository root, configure
the server URL and optional bearer token:

```sh
export TRUSTIFY_URL=https://trustify.example
export TRUSTIFY_TOKEN=your-token  # omit for anonymous access
```

Run an example with `uv`:

```sh
uv run --project python examples/python/server_info.py
uv run --project python examples/python/sbom_inventory.py --limit 20
uv run --project python examples/python/data_report.py --limit 100
```

`uv` creates and uses the project environment under `python/`; no global
`pip install` or environment activation is needed.

`TRUSTIFY_URL` defaults to `http://localhost:8080`. The data report counts
vulnerability severities in the returned page and shows the server-reported
totals; increase `--limit` to inspect more records.
