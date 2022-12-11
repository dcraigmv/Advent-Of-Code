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
        head = [10,10]
        knots = [copy([10,10]) for i in range(9)]
        history = [copy(knots[8])]

        for cmd in self.input:
            for i in range(int(cmd[1])):
                if cmd[0] == "R":
                    head[1] += 1
                if cmd[0] == "L":
                    head[1] -= 1
                if cmd[0] == "U":
                    head[0] += 1
                if cmd[0] == "D":
                    head[0] -= 1

                for i, knot in enumerate(knots):
                    lead_knot = knots[i-1]
                    if i == 0:
                        lead_knot = head

                    # update tail to follow
                    if (abs(lead_knot[0] - knot[0]) >= 2 or abs(lead_knot[1] - knot[1]) >= 2) \
                            and lead_knot[0] != knot[0] and lead_knot[1] != knot[1]:
                            knot[0] = knot[0] + (1 if (lead_knot[0] - knot[0]) > 0 else -1)
                            knot[1] = knot[1] + (1 if (lead_knot[1] - knot[1]) > 0 else -1)
                    else:
                        if abs(lead_knot[0] - knot[0]) >= 2 and lead_knot[1] == knot[1]:
                            # horizontal move
                            knot[0] = knot[0] + (1 if (lead_knot[0] - knot[0]) > 0 else -1)
                        if abs(lead_knot[1] - knot[1]) >= 2 and lead_knot[0] == knot[0]:
                            # virtical move
                            knot[1] = knot[1] + (1 if (lead_knot[1] - knot[1]) > 0 else -1)

                history.append(copy(knots[8]))

        return len(list(set([(x[0],x[1]) for x in history])))

if __name__ == "__main__":
    puzzle = Puzzle(map_function=lambda x:str(x).strip().upper().split(" "))
    print(puzzle.solution())
