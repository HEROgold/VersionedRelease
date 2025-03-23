"""Class to manage a changelog file."""


from datetime import UTC, date, datetime
from typing import ClassVar

from VersionedRelease.files import CHANGELOG
from VersionedRelease.helpers import get_delimiter
from VersionedRelease.version import Version


class Changelog:
    """Class to manage a changelog file."""

    _version: ClassVar[Version] = Version.get_current()
    _date: ClassVar[date] = datetime.now(tz=UTC).date()
    _changes: ClassVar[str] = ""

    @staticmethod
    def add_change(change: str) -> None:
        """Add a change to the changelog."""
        Changelog._changes += change

    @staticmethod
    def set_version(version: Version) -> None:
        """Set the version of the changelog."""
        Changelog._version = version

    @staticmethod
    def set_date(date: date) -> None:
        """Set the date of the changelog."""
        Changelog._date = date

    @staticmethod
    def write() -> None:
        """Write text to the changelog."""
        if len(Changelog._changes) <= 0:
            msg = "No changes to write to the changelog."
            raise ValueError(msg)
        with CHANGELOG.open("w") as f:
            f.write(get_delimiter() + "\n")
            f.write(f"Version: {Changelog._version}\n")
            f.write(f"Date: {Changelog._date}\n")
            f.write(Changelog._changes + f.read())

    @staticmethod
    def read() -> str:
        """Read the changelog."""
        with CHANGELOG.open() as f:
            return f.read()

    @staticmethod
    def clear() -> None:
        """Clear the changelog."""
        with CHANGELOG.open("w") as f:
            f.write("")


# TODO
# Add changelog based on github closed issues
# between last version and new version
# Indent by 2 spaces.
# Use tags from github issues to categorize
# the changes.
# Support for:
# Added, Changed, Fixed, Removed, Info
