"""Helper functions for the VersionedRelease package."""

from typing import LiteralString

delimiter_length = 99


def get_delimiter() -> LiteralString:
    """Get the delimiter for the changelog."""
    return "-" * delimiter_length
