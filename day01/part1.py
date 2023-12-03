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

    def solution(self):
        total = 0
        for line in self.input:
            for map in self.digit_map:
                line = re.replace
            numbers = re.findall(r'\d', line)
            total += int("" + numbers[0] + numbers[-1])
        return total


if __name__ == "__main__":
    puzzle = Puzzle()
    print(puzzle.solution())
