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
    def hand_score(self, hand: str) -> int:
        """
        Calc the numerical score for the hand, can be in ABC or XYZ notation
        rock:1 paper:2 scissors:3
        :param hand: str, a letter corresponding to the hand
        :return: int,    rock:1 paper:2 scissors:3
        """
        try:
            return ["A", "B", "C"].index(hand) + 1
        except ValueError:
            try:
                return ["X", "Y", "Z"].index(hand) + 1
            except ValueError:
                return 0

    def round_score(self, opponent_hand: str, my_hand: str) -> int:
        """
        Calc the numerical score for the round
        lose:0 draw:3 win:6
        :param opponent_hand: str, the hand to compare against
        :param my_hand: str, the hand to compare with
        :return: int, the score
        """
        opponent_score = self.hand_score(opponent_hand)
        my_score = self.hand_score(my_hand)

        # handle draw
        if opponent_score == my_score:
            return 3

        # handle wrap around cases
        if opponent_score == 1 and my_score == 3:
            return 0
        if opponent_score == 3 and my_score == 1:
            return 6

        # highest wins
        return (6 if my_score > opponent_score else 0)

    def solution(self):
        """
        Nothing special, loop through calling the other methods and then summing
        :return: int, sum of all scores for all rounds
        """
        scores = []
        for round in self.input:
            score = self.hand_score(round[1]) + self.round_score(*round)
            scores.append(score)

        return sum(scores)


if __name__ == "__main__":
    puzzle = Puzzle(map_function=lambda x:str(x).strip().upper().split(" "))
    print(puzzle.solution())
