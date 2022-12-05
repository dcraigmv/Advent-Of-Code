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
    def parse_stack_input(self) -> None:
        """
        Parse either a stack definition or a move command
        move commands are easy but stacks can be whitespace, my ide also trims
        trailing whitespace from lines so there is that to deal with
        :return: None, affects self.stacks and self.movements
        """

        self.stacks = []
        self.movements = []

        for line in self.input:
            # split move commands into the relevant information
            # move 1 from 2 to 1   ->  ["1", "2", "1"]
            move_cmd = re.split(r"\D+", line)

            # split line on either a box [X] and a space or a blank "   " (3 spaces) and a space,
            # the final stack will be the final list element
            # filter the split result for elements that are 4 spaces (a blank) or start with a [ (a box)
            # "[Z] [M] [P]"
            stack_row = list(filter(lambda s: s == "    " or s.startswith("["), re.split(r"(\[[A-Z]\] |    )", line)))

            if re.match(r"^move ", line):
                # movements
                self.movements.append(move_cmd[1:])
            elif len(stack_row) > 0:
                # stack starting position
                for i, box in enumerate(stack_row):

                    # create a new stack if one doesn't exist
                    if len(self.stacks) == i:
                        self.stacks.append([])

                    # append the letter character from the input to the end of this stack
                    if box is not None and box.strip() != "":
                        self.stacks[i].append(box.strip()[1])

        # at this point stacks will be reversed so flip them over
        for stack in self.stacks:
            stack.reverse()

    def solution(self) -> str:
        """
        Most of the work has already been done parsing the input so this method
        just slices elements off of, and appends them to, stacks, maintaining order.
        The stacks then have the last element taken and letters concatenated together
        :return: str, the last element letter of each stack   "DEHN"
        """

        for move in self.movements:
            # movements are still strings so int them and then zero index them
            from_i = int(move[1]) - 1
            to_i = int(move[2]) - 1

            # slice the stack into a variable and then remove that end slice from the original stack
            # this could be done in a range loop with pop, but slices also preserve order
            boxes = self.stacks[from_i][int(move[0]) * -1:]
            self.stacks[from_i] = self.stacks[from_i][0:int(move[0]) * -1]

            # add the box onto the end of the target stack
            self.stacks[to_i].extend(boxes)

        # take the last char from each stack
        top_boxes = [stack[-1] for stack in self.stacks]

        # cat the last box in each stack together to create the answer
        return "".join(top_boxes)


if __name__ == "__main__":
    puzzle = Puzzle(map_function=lambda x: str(x))
    puzzle.parse_stack_input()
    print(puzzle.solution())
