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

        priorities = []
        for bag in self.input:
            # split the bag contents into two compartments for comparison
            half_index = int(len(bag)/2)
            compartments = [bag[:half_index], bag[half_index:]]

            # collect any items that appear in both compartments
            duplicates = list(set([x for x in compartments[0] if x in compartments[1]]))
            assert len(duplicates) == 1 # we should only have one duplicate across compartments

            # convert the first duplicate item to it's priority and store
            priorities.append(self.item_priority(duplicates[0]))

        return sum(priorities)

if __name__ == "__main__":
    # convert each line character strings into a list of ordinal numbers a=1
    puzzle = Puzzle(map_function=lambda x:[ord(c) for c in str(x).strip()])
    print(puzzle.solution())
