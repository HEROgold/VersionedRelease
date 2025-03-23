"""Command line arguments for the versioned release script."""
from argparse import ArgumentParser, Namespace

parser = ArgumentParser(description="Versioned Release")
parser.add_argument(
    "--major",
    action="store_true",
    help="Increment the major version",
    default=False,
)
parser.add_argument(
    "--minor",
    action="store_true",
    help="Increment the minor version",
    default=False,
)
parser.add_argument(
    "--patch",
    action="store_true",
    help="Increment the patch version",
    default=False,
)

class Args(Namespace):
    """Container for parsed arguments."""

    major: bool
    minor: bool
    patch: bool

arguments = Args(*parser.parse_args())
