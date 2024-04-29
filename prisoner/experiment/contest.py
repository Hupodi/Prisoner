from typing import List
from itertools import combinations
import random

from prisoner.strategies.strategy import Strategy
from prisoner.experiment.match import Match


class Contest:
    """
    A class representing a full contest between a sert of strategies.
    - Each strategy is paired up against every other
    - Each match is of random length
    - Each match is played x times
    """

    def __init__(self, strategies: List[Strategy]):
        self.strategies = strategies

    def play_contest(self):
        for strategy_1, strategy_2 in combinations(self.strategies, 2):
            round_counts = random.randrange(150, 250)
            match = Match(
                strategy_1=strategy_1, strategy_2=strategy_2, rounds_count=round_counts
            )
            match.play_match()
