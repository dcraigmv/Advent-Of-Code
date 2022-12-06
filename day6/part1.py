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
        marker_length = 4
        # get the first and only line of the input mapper
        buffer = next(self.input)

        # starting at marker_length as there will be no full windows beforehand
        for i in range(marker_length, len(buffer)):
            # take a slice of the message and create a unique set, duplicates will be discarded
            unique = list(set(buffer[i-marker_length:i]))

            # if the set is the same length as the original slice, no duplicates
            # were discarded and the chars in the slice are all unique
            if len(unique) == marker_length:
                return i

if __name__ == "__main__":
    puzzle = Puzzle(map_function=lambda x:str(x).strip())
    print(puzzle.solution())
