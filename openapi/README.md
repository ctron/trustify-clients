# OpenAPI source

`openapi.yaml` is based on the Trustify `v0.6.2` release at commit
`b9d2627f83d189f0e7447b6bc0820f95bd061749`.

SHA-256: `08e625ceb260af20123f89a0a34ce182f544eb664e1c837026f22e261aa57551`

The checked-in spec corrects upstream response schemas: organization listings
return `PaginatedResults_OrganizationSummary`, weakness listings return
`PaginatedResults_WeaknessSummary`, and weakness details return
`WeaknessDetails`. Vulnerability filters use the field `id`, although response
objects expose that value as `identifier`.

To update it to another Trustify commit or tag, run:

```sh
scripts/sync-openapi.sh <git-ref>
```

The upstream specification is OpenAPI 3.1.0. The Rust `xtask` normalizes the
3.1 nullable-schema syntax and a few Trustify-spec input/media-type issues for
Progenitor 0.15.0. It keeps the canonical checked-in OpenAPI file unchanged;
the request hook restores the merge-patch content type at runtime. Run CI (or
`scripts/generate-rust.sh`) whenever this source or the generator changes.
