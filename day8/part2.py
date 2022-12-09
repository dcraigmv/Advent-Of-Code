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

class Puzzle(Base):
    def visible_distance(self, line_of_trees, visible):
        for index in range(0, len(line_of_trees)):
            height = line_of_trees[index]

            left_count = 0
            right_count = 0

            # check left
            for i in range(index-1, -1, -1):
                left_count += 1
                if line_of_trees[i] >= height:
                    break

            # check right
            for i in range(index+1, len(line_of_trees)):
                right_count += 1
                if line_of_trees[i] >= height:
                    break

            if visible[index] == 0:
                visible[index] = left_count * right_count
            else:
                visible[index] *= left_count * right_count

    def solution(self):
        trees = np.array(list(self.input), dtype=np.int32)
        width = len(trees[0])
        height = len(trees)

        false_col = [0] * width
        visible = []
        for _ in range(height):
            visible.append(copy(false_col))

        visible = np.array(visible, dtype=np.int32)

        # move down rows
        for i in range(0, height):
            self.visible_distance(trees[i], visible[i])

        # move along columns
        for i in range(0, width):
            self.visible_distance(trees[:,i], visible[:,i])

        return np.max(visible)

if __name__ == "__main__":
    puzzle = Puzzle(map_function=lambda x:[int(y) for y in str(x).strip()])
    print(puzzle.solution())
