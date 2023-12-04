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
import sys

from common.base import Base


class Puzzle(Base):
    def solution(self):
        cards = list(self.input)
        card_index = 0

        while card_index < len(cards):
            # clean away consecutive spaces
            card = re.sub(r' +', ' ', cards[card_index])
            # parse the input string
            numbers = re.findall(r'^Card (\d+): ([0-9 ]+) \| ([0-9 ]+)$', card)[0]
            # find numbers that appear in both lists
            intersection = [n for n in numbers[2].strip().split(" ") if n in numbers[1].strip().split(" ")]

            # append additional cards
            for i in range(len(intersection)):
                cards.append(cards[int(numbers[0]) + i])

            # print("%s intersection %s %d %s\n\n" % (numbers[0], intersection, len(cards), cards))

            card_index += 1

        # totals = {}
        # for card in cards:
        #     match = re.match(r'^Card (\d+)', card)
        #     totals[match.group(1)] = totals.get(match.group(1), 0) + 1
        #
        # print(totals)

        return card_index


if __name__ == "__main__":
    puzzle = Puzzle(map_function=lambda l:l.strip())
    print(puzzle.solution())
