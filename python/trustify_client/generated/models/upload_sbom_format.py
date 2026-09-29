from enum import StrEnum


class UploadSbomFormat(StrEnum):
    ADVISORY = "advisory"
    CISAKEV = "cisakev"
    CLEARLYDEFINED = "clearlydefined"
    CLEARLYDEFINEDCURATION = "clearlydefinedcuration"
    CSAF = "csaf"
    CVE = "cve"
    CWECATALOG = "cwecatalog"
    CYCLONEDX = "cyclonedx"
    NVD = "nvd"
    OSV = "osv"
    SBOM = "sbom"
    SPDX = "spdx"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
