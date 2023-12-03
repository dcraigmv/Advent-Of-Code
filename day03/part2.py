#!/usr/bin/env python3

"""
    A solution to the relevant day's puzzle on https://adventofcode.com/
"""

__author__ = "Daniel Craig"
__copyright__ = "Copyright 2023"
__version__ = "1.0.0"
__maintainer__ = "Daniel Craig"
__status__ = "Development"

import math
import re
import sys
from copy import copy

from common.base import Base


class Puzzle(Base):

    def is_symbol(self, char):
        return re.match(r'[^0-9\.]', char)

    def is_number(self, char):
        return re.match(r'[0-9]', char)

    def search_around(self, centre_row: int, centre_col: int) -> dict:
        found_numbers = {}
        for row in range(max(0, centre_row-1), centre_row+2):
            for col in range(max(0, centre_col-1), centre_col+2):
                try:
                    if self.is_number(self.input[row][col]):
                        number, start_row, start_col = self.number_at(row, col)
                        found_numbers[str(start_row)+":"+str(start_col)] = number

                except IndexError as e:
                    pass
        print("%s %s" % (self.input[centre_row][centre_col], found_numbers))

        return found_numbers

    def number_at(self, row: int, col: int) -> (int, int, int):
        number = ""
        try:
            while self.is_number(self.input[row][col]):
                col -= 1
        except IndexError as e:
            pass
        col += 1
        start_col = copy(col)
        try:
            while self.is_number(self.input[row][col]):
                number = number + self.input[row][col]
                col += 1
        except IndexError as e:
            pass

        if len(number) == 0:
            return 0

        return int(number), row, start_col

    def solution(self):
        self.input = list(self.input)
        symbol_count = 0
        gears = []
        for row in range(len(self.input)):
            for col in range(len(self.input[row])):
                if self.input[row][col] == "*":
                    symbol_count += 1
                    # search around this position
                    new_part_numbers = self.search_around(row, col)
                    if len(new_part_numbers.keys()) == 2:
                        gears.append(math.prod(new_part_numbers.values()))

        print("Found %d symbols" % symbol_count)
        return sum(gears)


if __name__ == "__main__":
    puzzle = Puzzle(map_function=lambda l:l.strip())
    print(puzzle.solution())
