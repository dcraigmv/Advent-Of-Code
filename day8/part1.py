#!/usr/bin/env python3

"""
    A solution to the relevant day's puzzle on https://adventofcode.com/2022
"""

__author__ = "Daniel Craig"
__copyright__ = "Copyright 2022"
__version__ = "1.0.0"
__maintainer__ = "Daniel Craig"
__status__ = "Development"

import numpy as np
from colorama import Fore, Style

from common.base import Base


class Puzzle(Base):
    def is_visible_from_edge(self, line_of_trees: np.ndarray, visible: np.ndarray):
        """
        Loop through the provided line of trees (could be row could be column)
        and determine if it's visible

        :param line_of_trees: ndarray a slice of the input array containing heights
        :param visible: ndarray the corresponding visibility slice to record if it is visible from an edge
        :return:
        """
        for index in range(1, len(line_of_trees) - 1):
            # get the height of the current tree
            height = line_of_trees[index]

            # we default to visible as it's easier to switch it off when you get to
            # a taller tree
            visible_from_left = True
            visible_from_right = True

            # check left
            for i in range(0, index):
                if line_of_trees[i] >= height:
                    visible_from_left = False
                    break

            # check right
            for i in range(len(line_of_trees) - 1, index, -1):
                if line_of_trees[i] >= height:
                    visible_from_right = False
                    break

            visible[index] = visible[index] or visible_from_left or visible_from_right

    def print_forest(self, trees, visible):
        for i, row in enumerate(trees):
            for j, col in enumerate(row):
                print((Fore.GREEN if visible[i, j] else Fore.BLACK) + str(col), end="")
            print()
        print(Style.RESET_ALL)

    def solution(self):
        # numpy the input so that we can nicely slice it in two dimensions
        trees = np.array(list(self.input), dtype=np.int32)

        # calc overall dimensions of input grid
        width = len(trees[0])
        height = len(trees)

        # create a duplicate of the input grid containing booleans
        # to signify if a tree is visible from an endge
        visible = [[False] * width for _ in range(height)]
        visible = np.array(visible, dtype=bool)

        # set the four edges to visible True
        visible[0, :] = True
        visible[len(visible) - 1, :] = True
        visible[:, 0] = True
        visible[:, len(visible[0]) - 1] = True

        # move down rows
        for i in range(1, len(trees) - 1):
            self.is_visible_from_edge(trees[i], visible[i])

        # move along columns
        for i in range(1, height - 1):
            self.is_visible_from_edge(trees[:, i], visible[:, i])

        # for debug print out the input with some colouring
        self.print_forest(trees, visible)

        # sum all of the visible trees True == 1
        return np.sum(visible)


if __name__ == "__main__":
    puzzle = Puzzle(map_function=lambda x: [int(y) for y in str(x).strip()])
    print(puzzle.solution())
