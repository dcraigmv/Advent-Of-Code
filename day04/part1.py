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
    def solution(self):
        score = 0
        for card in self.input:
            card = re.sub(r' +', ' ', card)
            numbers = re.findall(r'^Card \d+: ([0-9 ]+) \| ([0-9 ]+)$', card)[0]
            print(numbers)
            intersection = [n for n in numbers[1].strip().split(" ") if n in numbers[0].strip().split(" ")]
            print("intersection %s %d" % (intersection, 1 * pow(2, len(intersection)-1)))
            score += int(1 * pow(2, len(intersection)-1))
        return score


if __name__ == "__main__":
    puzzle = Puzzle(map_function=lambda l:l.strip())
    print(puzzle.solution())
