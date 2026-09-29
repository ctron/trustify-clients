from enum import StrEnum


class Relationship(StrEnum):
    ANCESTOR_OF = "ancestor_of"
    BUILD_TOOL = "build_tool"
    CONTAINS = "contains"
    DEPENDENCY = "dependency"
    DESCRIBES = "describes"
    DEV_DEPENDENCY = "dev_dependency"
    DEV_TOOL = "dev_tool"
    EXAMPLE = "example"
    GENERATES = "generates"
    OPTIONAL_DEPENDENCY = "optional_dependency"
    PACKAGE = "package"
    PROVIDED_DEPENDENCY = "provided_dependency"
    RUNTIME_DEPENDENCY = "runtime_dependency"
    TEST_DEPENDENCY = "test_dependency"
    UNDEFINED = "undefined"
    VARIANT = "variant"

    def __str__(self) -> str:
        return str(self.value)
