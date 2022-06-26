#!/usr/bin/env python3

from .CLI import parse_args
from .mdtree import MakeIndex


def main():
    args = parse_args()

    Indexer = MakeIndex(
        root_dir=args.directory,
        gitignore=args.gitignore,
        write=bool(args.output),
    )

    output = Indexer.generate()
    if args.quiet:
        print(output)

    if args.output:
        Indexer.write(args.output)


if __name__ == '__main__':
    main()
