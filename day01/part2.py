#!/usr/bin/env python3

"""
    A solution to the relevant day's puzzle on https://adventofcode.com/
"""

__author__ = "Daniel Craig"
__copyright__ = "Copyright 2023"
__version__ = "1.0.0"
__maintainer__ = "Daniel Craig"
__status__ = "Development"

import re

from common.base import Base


class Puzzle(Base):
    digit_map = dict(
        one=1,
        two=2,
        three=3,
        four=4,
        five=5,
        six=6,
        seven=7,
        eight=8,
        nine=9
    )

    def resolve_number(self, number):
        return str(self.digit_map.get(number, number))

    def solution(self):
        total = 0
        search_pattern = re.compile("(?=(\d|" + "|".join(self.digit_map.keys()) + "))")
        for line in self.input:
            numbers = re.findall(search_pattern, line)

            # print("%s    %s  %s" % (line, numbers[0], numbers[-1]))
            total += int("" + self.resolve_number(numbers[0]) + self.resolve_number(numbers[-1]))
        return total


if __name__ == "__main__":
    puzzle = Puzzle()
    print(puzzle.solution())
