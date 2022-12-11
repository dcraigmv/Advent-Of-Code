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

from common.base import Base

class Puzzle(Base):
    def solution(self):
        head = [0,0]
        tail = [0,0]
        history = [copy(tail)]

        for cmd in self.input:
            # loop through the command one step at a time
            for i in range(int(cmd[1])):
                if cmd[0] == "R":
                    head[1] += 1
                if cmd[0] == "L":
                    head[1] -= 1
                if cmd[0] == "U":
                    head[0] += 1
                if cmd[0] == "D":
                    head[0] -= 1

                # update tail to follow
                if (abs(head[0] - tail[0]) >= 2 or abs(head[1] - tail[1]) >= 2) \
                        and head[0] != tail[0] and head[1] != tail[1]:
                        tail[0] += (1 if (head[0] - tail[0]) > 0 else -1)
                        tail[1] += (1 if (head[1] - tail[1]) > 0 else -1)
                else:
                    if abs(head[0] - tail[0]) >= 2 and head[1] == tail[1]:
                        # horizontal move
                        tail[0] += (1 if (head[0] - tail[0]) > 0 else -1)
                    if abs(head[1] - tail[1]) >= 2 and head[0] == tail[0]:
                        # virtical move
                        tail[1] += (1 if (head[1] - tail[1]) > 0 else -1)

                history.append(copy(tail))

        return len(list(set([tuple(x) for x in history])))

if __name__ == "__main__":
    puzzle = Puzzle(map_function=lambda x:str(x).strip().upper().split(" "))
    print(puzzle.solution())
