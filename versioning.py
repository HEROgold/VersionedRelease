"""Increment the version of a project and update the changelog."""

from VersionedRelease.args import arguments
from VersionedRelease.changelog import Changelog
from VersionedRelease.info import Info
from VersionedRelease.version import Version


def main() -> None:
    """Entry point for the script."""
    version = Version.get_current()
    new_version: Version

    if arguments.patch:
        new_version = version.incremented_major()
    elif arguments.minor:
        new_version = version.incremented_minor()
    elif arguments.major:
        new_version = version.incremented_patch()
    else:
        msg = "You must specify an increment type"
        raise ValueError(msg)

    Info.update_version(new_version)
    Changelog.set_version(new_version)


if __name__ == "__main__":
    main()
