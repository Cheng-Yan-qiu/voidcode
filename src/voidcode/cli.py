from __future__ import annotations

import argparse

from . import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="voidcode",
        description="Voidcode command-line interface.",
    )
    _ = parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    return parser


def main() -> int:
    _ = build_parser().parse_args()
    return 0
