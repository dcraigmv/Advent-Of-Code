#!/usr/bin/env python3

"""
    A solution to the relevant day's puzzle on https://adventofcode.com/2022
"""

__author__ = "Daniel Craig"
__copyright__ = "Copyright 2022"
__version__ = "1.0.0"
__maintainer__ = "Daniel Craig"
__status__ = "Development"

from common.base import Base


class Puzzle(Base):
    def solution(self):
        return

if __name__ == "__main__":
    puzzle = Puzzle(map_function=lambda x:str(x).strip())
    print(puzzle.solution())
