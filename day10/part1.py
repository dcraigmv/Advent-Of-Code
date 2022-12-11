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
    def output_signal_strength(self, cycle: int, x_register: int, signal_strengths: list) -> None:
        """
        Check if we are at the end of a cycle and multiply the counters together
        to get a "signal strength

        :param cycle: int the counter of which loop we are in
        :param x_register: int the current register value
        :param signal_strengths: list, a list to store the signal strengths
        :return: None
        """

        # if we are at the end of a certain cycle, calc signal stength
        if cycle in [20, 60, 100, 140, 180, 220]:
            signal_strengths.append(cycle * x_register)

    def solution(self):
        cycle = 0
        x_register = 1
        signal_strengths = []

        for line in self.input:
            cycle += 1
            self.output_signal_strength(cycle, x_register, signal_strengths)

            # only pick up addx commands, noops are useless
            match = re.match(r"^addx (-?\d+)$", line)
            if match is not None:
                cycle += 1 # addx takes two cycles
                self.output_signal_strength(cycle, x_register, signal_strengths)

                # increase the x register
                x_register += int(match.group(1))

        # return the total signal strengths
        return sum(signal_strengths)

if __name__ == "__main__":
    puzzle = Puzzle(map_function=lambda x:str(x).strip())
    print(puzzle.solution())
