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

from common.base import Base


class Puzzle(Base):
    def visible_distance(self, line_of_trees: np.ndarray, visible: np.ndarray):
        for index in range(0, len(line_of_trees)):
            # get the height of the current tree
            height = line_of_trees[index]

            left_count = 0
            right_count = 0

            # check left
            for i in range(index - 1, -1, -1):
                # total up the number of visible trees
                # until we get to a tree equal or taller
                left_count += 1
                if line_of_trees[i] >= height:
                    break

            # check right
            for i in range(index + 1, len(line_of_trees)):
                # total up the number of visible trees
                # until we get to a tree equal or taller
                right_count += 1
                if line_of_trees[i] >= height:
                    break

            # either set or increase the visible tree count
            if visible[index] == 0:
                visible[index] = left_count * right_count
            else:
                visible[index] *= left_count * right_count

    def solution(self):
        # numpy the input so that we can nicely slice it in two dimensions
        trees = np.array(list(self.input), dtype=np.int32)

        # calc overall dimensions of input grid
        width = len(trees[0])
        height = len(trees)

        # create a duplicate of the input grid containing booleans
        # to signify if a tree is visible from an endge
        visible = [[0] * width for _ in range(height)]
        visible = np.array(visible, dtype=int)

        # move down rows
        for i in range(0, height):
            self.visible_distance(trees[i], visible[i])

        # move along columns
        for i in range(0, width):
            self.visible_distance(trees[:, i], visible[:, i])

        # get the largest visible distance
        return np.max(visible)


if __name__ == "__main__":
    puzzle = Puzzle(map_function=lambda x: [int(y) for y in str(x).strip()])
    print(puzzle.solution())
