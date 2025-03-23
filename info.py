"""Info class for handling the project's information."""

import json

from VersionedRelease.conifg import JSON_INDENT
from VersionedRelease.version import Version

from files import INFO


class Info:
    """Container for project information."""

    @staticmethod
    def update_version(new: Version) -> None:
        """Update the version in the info.json file."""
        with INFO.open("w") as f:
            data = json.load(f)
            data["version"] = str(new)
            json.dump(data, f, indent=JSON_INDENT)
