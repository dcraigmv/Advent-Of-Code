#!/usr/bin/env python3

"""
    A solution to the relevant day's puzzle on https://adventofcode.com/2022
"""

__author__ = "Daniel Craig"
__copyright__ = "Copyright 2022"
__version__ = "1.0.0"
__maintainer__ = "Daniel Craig"
__status__ = "Development"

import re
from copy import copy

from common.base import Base

def traverse(path, structure):
    current_dir=structure
    for dir in path:
        current_dir = current_dir["children"][dir]
    return current_dir

def total_sizes(structure: dict) -> dict:
    dir_sizes = {}
    total_child_sizes(structure, dir_sizes)
    return dir_sizes

def total_child_sizes(structure: dict, dir_sizes: dict) -> int:
    for child in structure.get("children", {}).values():
        structure["size"] += total_child_sizes(child, dir_sizes)

    # just directories with contents
    if len(structure.get("children", {}).keys()) > 0:
        abs_dir_path = "/".join(structure["path"]) + structure["name"]
        dir_sizes[abs_dir_path] = structure["size"]

    return structure["size"]

class Puzzle(Base):
    def solution(self):
        dir_structure = dict(size=0, children={}, name="/", path=[])
        pwd = []

        for line in self.input:
            cd_cmd = re.match(r"^\$ cd ([a-z\/\.]+)", line, re.IGNORECASE)
            if cd_cmd is not None:
                subdir = cd_cmd.group(1)

                # change directory
                if subdir == "/":
                    pwd = []
                elif subdir == "..":
                    pwd.pop()
                else:
                    pwd.append(subdir)

            dir_output = re.match(r"^dir ([a-z0-9]+)", line, re.IGNORECASE)
            if dir_output is not None:
                # add dir structure
                parent = traverse(pwd, dir_structure)
                if dir_output.group(1) not in parent["children"].keys():
                    parent["children"][dir_output.group(1)] = dict(size=0, children={}, name=dir_output.group(1), path=copy(pwd))


            dir_output = re.match(r"^([0-9]+) ([a-z0-9\.]+)", line, re.IGNORECASE)
            if dir_output is not None:
                parent = traverse(pwd, dir_structure)
                if dir_output.group(2) not in parent["children"].keys():
                    parent["children"][dir_output.group(2)] = dict(size=int(dir_output.group(1)), name=dir_output.group(2))

        dir_sizes = total_sizes(dir_structure)

        total_disk_space = 70000000
        required_disk_space = 30000000
        total_used = dir_sizes["/"]
        to_free = total_used - (total_disk_space - required_disk_space)
        for dir in sorted(dir_sizes.values()):
            if dir > to_free:
                return dir

if __name__ == "__main__":
    puzzle = Puzzle(map_function=lambda x:str(x).strip())
    print(puzzle.solution())
