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
    def parse_notes(self):
        """
        The lines in the input are in sections so parse them into a monkeys object attr
        :return: None
        """

        # store monkey observations and a pointer to the current monkey
        self.monkeys = []
        monkey_index = 0

        for line in self.input:

            # get the change in monkey id
            monkey_id_match = re.match(r"^Monkey (\d+):$", line)
            if monkey_id_match is not None:
                monkey_index = int(monkey_id_match.group(1))

                # instantiate monkey data structure for a new monkey
                if len(self.monkeys) == monkey_index:
                    self.monkeys.append(dict(
                        id=monkey_index,
                        items=[],
                        items_inspected=0,
                        operation="x",
                        test=1,
                        true=0,
                        false=0
                    ))

            # items and their worry level
            items_match = re.match(r"Starting items: ([\d, ]+)$", line)
            if items_match is not None:
                self.monkeys[monkey_index]['items'] = [int(i.strip()) for i in items_match.group(1).split(",")]

            # a string equasion to eval each time a monkey inspects and item
            opperation_match = re.match(r"Operation: new = old ([\+\*]) (\d+|old)$", line)
            if opperation_match is not None:
                self.monkeys[monkey_index]['operation'] = "old %s %s" % (opperation_match.group(1), opperation_match.group(2))

            # the test (normally devisible by x) used by each monkey
            test_match = re.match(r"Test: divisible by (\d+)$", line)
            if test_match is not None:
                self.monkeys[monkey_index]['test'] = int(test_match.group(1))

            # the monkey to throw to if the above test is true
            true_match = re.match(r"If true: throw to monkey (\d+)$", line)
            if true_match is not None:
                self.monkeys[monkey_index]['true'] = int(true_match.group(1))

            # the monkey to throw to if the above tests is false
            false_match = re.match(r"If false: throw to monkey (\d+)$", line)
            if false_match is not None:
                self.monkeys[monkey_index]['false'] = int(false_match.group(1))

    def solution(self):
        rounds = 20
        for round in range(rounds):
            # for each monkey
            for monkey in self.monkeys:
                # for each of the monkey's items
                for item in monkey["items"]:
                    # eval the monkey's operation and then divide by the universal three
                    item = (lambda old:eval(monkey["operation"]))(item) // 3

                    # throw to a monkey depending on tests
                    if item % monkey["test"] == 0:
                        self.monkeys[monkey["true"]]["items"].append(item)
                    else:
                        self.monkeys[monkey["false"]]["items"].append(item)

                    # the monkey has looked at an item, increment it's inspection counter
                    monkey["items_inspected"] += 1

                # all the monkey's items have been looked at so clear it's inventory
                monkey["items"] = []

        # sort the monkeys and return the product of the top two's inspection counters
        most_active_monkeys = sorted(self.monkeys, key=lambda x:x["items_inspected"], reverse=True)
        return most_active_monkeys[0]["items_inspected"] * most_active_monkeys[1]["items_inspected"]

if __name__ == "__main__":
    puzzle = Puzzle(map_function=lambda x:str(x).strip())
    puzzle.parse_notes()
    print(puzzle.solution())
