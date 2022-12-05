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
    def solution(self):
        overlaps = []
        for elves in self.input:
            # binary AND comparison so that we get the intersection of both elves' sections
            # 0111000 | 0001110   ==  0001000

            overlap = elves[0] & elves[1]

            # 1 means they work in the same section
            overlaps.append(1 if overlap else 0)

        # total up the overlaps
        return sum(overlaps)


if __name__ == "__main__":
    def parse_section_assignments(line: str) -> list:
        """

        :param line: str, x-x,y-y section definition
        :return: list of base 2 integers representing
                    the binary encoding of the sections to be worked
        """

        # split each elf's section definition and then split each section into start and end ints
        elves = [x.strip().split("-") for x in line.strip().split(",")]
        bin_elves = []
        for elf in elves:
            start = int(elf[0])
            end = int(elf[1])

            # build a binary string 1 means the elf is working that section 0 means not
            # 2-4  ->  ...001110 the maximum section number seems to be 100 so lpad with zeros
            elf = (["0"] * (100 - end)) + (["1"] * (1 + end - start)) + (["0"] * (start - 1))
            bin_elves.append(int("".join(elf), 2))

        return bin_elves


    puzzle = Puzzle(map_function=parse_section_assignments)
    print(puzzle.solution())
