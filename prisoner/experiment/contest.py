from typing import List
from itertools import combinations
import random

import numpy as np

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
        self._strategies = strategies
        self._points = [0 for _ in range(len(strategies))]

    def play_contest(self) -> None:
        """
        Play the entire contest
        """

        for strategy_1, strategy_2 in combinations(self._strategies, 2):
            self.play_match_up(strategy_1, strategy_2)
        self._normalise_points()

    def play_match_up(self, strategy_1: Strategy, strategy_2: Strategy):
        """
        Play a match up between two strategies, repeating the match MATCH_REPLAY_COUNT times
        """
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

        self._points[self._strategies.index(strategy_1)] += (
            sum(points_1) / MATCH_REPLAY_COUNT
        )
        self._points[self._strategies.index(strategy_2)] += (
            sum(points_2) / MATCH_REPLAY_COUNT
        )

    def _normalise_points(self):
        """
        Normalise points for each strategy, dividing by the amount of face-up played (len - 1)
        """
        self._points = [points / (len(self._strategies) - 1) for points in self._points]

    def __repr__(self):
        """
        Represent the contest
        """
        repr_str = ""
        sorting_index = np.argsort(self._points)
        for index in reversed(sorting_index):
            repr_str += (
                f"{self._strategies[index].name}: {round(self._points[index], 2)}\n"
            )
        return repr_str
