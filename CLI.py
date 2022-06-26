#!/usr/bin/env python3

'''
A CLI builder for the mdtree program
'''

import argparse
from . import __version__

__banner = """
          _  _
 _____  _| || |_  ___  ___  ___
|     || . ||  _||  _|| -_|| -_|
|_|_|_||___||_|  |_|  |___||___|
                                """


def parse_args():
    print(__banner)
    parser = argparse.ArgumentParser(
        prog="mdtree",
        description="mdtree: make a Linkable Markdown File Tree with minimal effort!",
        epilog="Thank you for using mdtree!",
    )

    parser.version = f"mdtree v{__version__}"

    parser.add_argument(
        "-d",
        "--directory",
        type=str,
        default=".",
        help="Start directory for the tree",
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
    )

    parser.add_argument(
        "-i",
        "--gitignore",
        action="store_true",
        help="Ignore files listed in .gitignore",
    )

    parser.add_argument(
        "-o",
        "--output",
        nargs="?",
        type=str,
        help="Write to a file"
    )

    parser.add_argument(
        "-q",
        "--quiet",
        action="store_false",
        help="Print to stdout"

    )

    return parser.parse_args()
