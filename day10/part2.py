#!/usr/bin/env python3

"""
    A solution to the relevant day's puzzle on https://adventofcode.com/2022
"""

__author__ = "Daniel Craig"
__copyright__ = "Copyright 2022"
__version__ = "1.0.0"
__maintainer__ = "Daniel Craig"
__status__ = "Development"

import re

from common.base import Base


class Puzzle(Base):
    def render(self, cycle: int, x_register: int) -> None:
        """
        Print out either a . or # depending on the value of cycle and register params
        like a scanning CRT would

        :param cycle: int the counter of which loop we are in
        :param x_register: int the current register value
        :return: None
        """
        screen_width = 40
        if (cycle % screen_width) >= x_register and (cycle % screen_width) <= x_register + 2:
            print("#", end="")
        else:
            print(".", end="")

        # if we are the end of the screen, print a carriage return
        if (cycle % screen_width) == 0:
            print()

    def solution(self):
        cycle = 0
        x_register = 1

        for line in self.input:
            cycle += 1
            self.render(cycle, x_register)

            # only pick up addx commands, noops are useless
            match = re.match(r"^addx (-?\d+)$", line)
            if match is not None:
                cycle += 1 # addx takes two cycles
                self.render(cycle, x_register)

                # increase the x register
                x_register += int(match.group(1))

if __name__ == "__main__":
    puzzle = Puzzle(map_function=lambda x:str(x).strip())
    puzzle.solution()
