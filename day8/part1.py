#!/usr/bin/env python3

"""
    A solution to the relevant day's puzzle on https://adventofcode.com/2022
"""

__author__ = "Daniel Craig"
__copyright__ = "Copyright 2022"
__version__ = "1.0.0"
__maintainer__ = "Daniel Craig"
__status__ = "Development"

from copy import copy

import numpy as np

from common.base import Base
from colorama import Fore, Style

class Puzzle(Base):
    def is_visible_from_edge(self, line_of_trees, visible):
        for index in range(1, len(line_of_trees)-1):
            height = line_of_trees[index]
            visible_from_left = True
            visible_from_right = True

            # check left
            for i in range(0, index):
                if line_of_trees[i] >= height:
                    visible_from_left = False
                    break

            # check right
            for i in range(len(line_of_trees)-1, index, -1):
                if line_of_trees[i] >= height:
                    visible_from_right = False
                    break

            visible[index] = visible[index] or visible_from_left or visible_from_right

    def print_forest(self, trees, visible):
        for i, row in enumerate(trees):
            for j, col in enumerate(row):
                print((Fore.GREEN if visible[i,j] else Fore.BLACK) + str(col), end="")
            print()
        print(Style.RESET_ALL)

    def solution(self):
        trees = np.array(list(self.input), dtype=np.int32)
        width = len(trees[0])
        height = len(trees)

        false_col = [False] * width
        visible = []
        for _ in range(height):
            visible.append(copy(false_col))

        visible = np.array(visible, dtype=bool)
        visible[0,:] = True
        visible[len(visible)-1,:] = True
        visible[:,0] = True
        visible[:,len(visible[0])-1] = True

        # move down rows
        for i in range(1, len(trees)-1):
            self.is_visible_from_edge(trees[i], visible[i])

        # move along columns
        for i in range(1, height-1):
            self.is_visible_from_edge(trees[:,i], visible[:,i])

        self.print_forest(trees, visible)


        return np.sum(visible)

if __name__ == "__main__":
    puzzle = Puzzle(map_function=lambda x:[int(y) for y in str(x).strip()])
    print(puzzle.solution())
