"""Version class for handling version information."""
import json
from typing import Self

from attr import dataclass
from VersionedRelease.files import INFO


@dataclass
class Version:
    """Container for version information."""

    major: int
    minor: int
    patch: int

    def __str__(self) -> str:
        """Get the version as preferred in info.json."""
        return f"{self.major}.{self.minor}.{self.patch}"

    @staticmethod
    def get_current() -> "Version":
        """Get the current version from info.json."""
        with INFO.open() as f:
            data = json.load(f)
            return Version(*Version.get_parts(data["version"]))

    @staticmethod
    def get_parts(version: str) -> tuple[int, int, int]:
        """Get the parts of the version."""
        version_parts = version.split(".")
        return (
            int(version_parts[0]),
            int(version_parts[1]),
            int(version_parts[2]),
        )

    def incremented_patch(self: Self) -> "Version":
        """Increment the patch version. Return a new Version."""
        return Version(self.major, self.minor, self.patch + 1)

    def incremented_minor(self: Self) -> "Version":
        """Increment the minor version. Return a new Version."""
        return Version(self.major, self.minor + 1, 0)

    def incremented_major(self: Self) -> "Version":
        """Increment the major version. Return a new Version."""
        return Version(self.major + 1, 0, 0)
