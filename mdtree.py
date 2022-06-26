#!/usr/bin/env python3

import os
from os import path

from urllib.parse import quote


class MakeIndex:

    def __init__(self, root_dir: str, gitignore: bool = False, write: bool = False):
        if not path.isdir(root_dir):
            raise NotADirectoryError(f"[!] {root_dir} is not a directory!")
        self._root_dir = root_dir.rstrip(os.sep)

        if gitignore:
            if not (path.exists(f"{self._root_dir}{os.sep}.gitignore") and path.isfile(".gitignore")):
                raise FileNotFoundError("[!] .gitignore not found")
        self._ignore = gitignore
        self._gitignore_location = f"{self._root_dir}{os.sep}.gitignore"

    def make_md_link(self, file_name: str) -> str:
        return f"[{path.basename(file_name)}]({quote(file_name)})"

    def ignore_files(self):
        if not self._ignore:
            return []

        ignore_extensions = []

        with open(self._gitignore_location, "r") as gitignore:
            ignore_contents = gitignore.read().split("\n")

            for extension in filter(lambda ex: ex or ex.startswith("#"), ignore_contents):
                extension = extension.strip("*")
                if extension.startswith("."):
                    ignore_extensions.append(extension)

        return ignore_extensions

    def list_files(self, directory: str) -> iter:
        if not hasattr(self, "ignore_extensions"):
            self.ignore_extensions = self.ignore_files()

        def is_valid(filename) -> bool:
            if "." in filename:
                return not any((filename.endswith(ex) for ex in self.ignore_extensions))
            return True
        yield from filter(is_valid, os.listdir(directory))

    def make_tree(self, curr_dir: str, indent_level: int = 0, output: str = "") -> str:
        if path.isfile(curr_dir):
            return output + "\t" * indent_level + f"- {self.make_md_link(curr_dir)}\n"

        output += "\t" * indent_level + f"- {path.basename(curr_dir)}\n"

        for f in self.list_files(curr_dir):
            if not f.startswith("."):
                output = self.make_tree(f"{curr_dir}{os.sep}{f}", indent_level+1, output)
        return output

    def generate(self) -> str:
        self.tree = self.make_tree(self._root_dir)
        return self.tree

    def write(self, filename) -> str:
        with open(filename, "w") as output_file:
            if not hasattr(self, "tree"):
                raise AttributeError("[!] Tree has not been generated yet")
            output_file.write(self.tree)
