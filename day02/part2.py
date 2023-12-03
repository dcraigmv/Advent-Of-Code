#!/usr/bin/env python3

"""
    A solution to the relevant day's puzzle on https://adventofcode.com/
"""

__author__ = "Daniel Craig"
__copyright__ = "Copyright 2023"
__version__ = "1.0.0"
__maintainer__ = "Daniel Craig"
__status__ = "Development"

import math
import re

from common.base import Base


class Puzzle(Base):

    games: dict = {}

    limit_red: int = 12
    limit_green: int = 13
    limit_blue: int = 14

    def solution(self):
        self.parse_game_input(self.input)

        powers = []
        for id, game in self.games.items():
            minimums = dict(
                red=max([r["red"] for r in game]),
                green=max([r["green"] for r in game]),
                blue=max([r["blue"] for r in game])
            )
            powers.append(math.prod(minimums.values()))

        return sum(powers)

    def parse_game_input(self, input: list):
        for game in input:
            match = re.match(r'^Game (\d+): (.*)$', game)
            game_id = int(match.group(1))

            if game_id not in self.games.keys():
                self.games[game_id] = []

            for round_str in match.group(2).split(";"):
                round = dict(red=0,green=0,blue=0)

                for cube in round_str.split(","):
                    parts = cube.strip().split(" ")
                    round[parts[1]] = int(parts[0])
                self.games[game_id].append(round)


if __name__ == "__main__":
    puzzle = Puzzle()
    print(puzzle.solution())
