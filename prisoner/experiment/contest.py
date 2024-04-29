from typing import List
from itertools import combinations
import random

from prisoner.strategies.strategy import Strategy
from prisoner.experiment.match import Match


MATCH_REPLAY_COUNT = 5


class Contest:
    """
    A class representing a full contest between a sert of strategies.
    - Each strategy is paired up against every other
    - Each match is of random length
    - Each match is played x times
    """

    def __init__(self, strategies: List[Strategy]) -> None:
        self.strategies = strategies
        self.points = [0 for _ in range(len(strategies))]

    def play_contest(self) -> None:
        """
        Play the entire contest
        """

        for strategy_1, strategy_2 in combinations(self.strategies, 2):

            points_1 = []
            points_2 = []
            for match_count in range(MATCH_REPLAY_COUNT):
                round_counts = random.randrange(150, 250)
                match = Match(
                    strategy_1=strategy_1, strategy_2=strategy_2, rounds_count=round_counts
                )
                points = match.play_match()
                points_1.append(points[0])
                points_2.append(points[1])

            self.points[self.strategies.index(strategy_1)] += points_1
            self.points[self.strategies.index(strategy_2)] += points_2

    def _get_normalised_points(self):
        """
        Normalise points for each strategy, dividing by the amount of face-up played (len - 1)
        """
        self.points = [points / (len(self.strategies) - 1) for points in self.points]
