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
    priority_map = []

    def item_priority(self, item_ord: int) -> int:
        """
        convert letters to a "priority" number, lower case first
        :param item_ord: int, ordinal number of a character
        :return: int 1-52
        """
        # a=1 b=2 ... A=27 ...
        return self.priority_map.index(item_ord) + 1

    def solution(self):
        # create a list of letter ordinals lower case first, index is used for priority
        # should be done in __init__
        self.priority_map = [x for x in list(range(97, 123)) + list(range(65, 91))]

        # convert input map to list because maps don't have a length
        self.input = list(self.input)

        group_size = 3
        priorities = []

        # loop through the bags hopping three at a time
        for i in range(0, len(self.input), group_size):
            # get all the bags for this group
            group_bags = self.input[i:i + group_size]

            # using the first bag contents as a guide, find the item that is in all three bags
            duplicates = list(set([x for x in group_bags[0] if x in group_bags[1] and x in group_bags[2]]))
            assert len(duplicates) == 1

            # convert the first duplicate item to it's priority and store
            priorities.append(self.item_priority(duplicates[0]))

        return sum(priorities)

if __name__ == "__main__":
    # convert each line character strings into array of ordinal numbers a=1
    puzzle = Puzzle(map_function=lambda x:[ord(c) for c in str(x).strip()])
    print(puzzle.solution())
