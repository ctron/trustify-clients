CARGO ?= cargo
ARGS ?=

.PHONY: check test run python-test python-generate

check:
	$(CARGO) clippy --manifest-path rust/Cargo.toml --workspace --all-targets --all-features -- -D warnings

test:
	$(CARGO) nextest run --manifest-path rust/Cargo.toml --workspace

run:
	$(CARGO) run --manifest-path rust/Cargo.toml -p trustify-client --example info -- $(ARGS)

python-test:
	uv run --project python python -m unittest discover -s python/tests

python-generate:
	scripts/generate-python.sh
