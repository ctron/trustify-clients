from enum import StrEnum


class ClearlyDefinedPackageType(StrEnum):
    COMPOSER = "composer"
    CRATE = "crate"
    DEB = "deb"
    GEM = "gem"
    GIT = "git"
    GO = "go"
    MAVEN = "maven"
    NPM = "npm"
    NUGET = "nuget"
    POD = "pod"
    PYPI = "pypi"

    def __str__(self) -> str:
        return str(self.value)
