from typing import Tuple

from prisoner.parameters.rewards import REWARDS
from prisoner.strategies.strategy import Strategy


class Match:
    """
    Class representing a prisoner's dilemma match between two strategies
    """

    def __init__(
        self, strategy_1: Strategy, strategy_2: Strategy, rounds_count: int = 200
    ):
        self._strategy_1 = strategy_1
        self._strategy_2 = strategy_2
        self._rounds_count = rounds_count
        self._history = {
            0: [],
            1: [],
        }
        self._points = {
            0: 0,
            1: 0,
        }

    def play_match(self) -> Tuple[float, float]:
        """
        Play a full match between the two strategies
        """
        for round_number in range(self._rounds_count):
            self._play_single_round()
        return self._get_points_per_round()

    def _play_single_round(self) -> None:
        """
        Play a single step, a single dilemma
        """
        decision_1 = self._strategy_1.decide_step(
            self_history=self._history[0], opponent_history=self._history[1]
        )
        self._history[0].append(decision_1)
        decision_2 = self._strategy_2.decide_step(
            self_history=self._history[1], opponent_history=self._history[0]
        )
        self._history[1].append(decision_2)

        self._increment_points(decision_1, decision_2)

    def _increment_points(self, decision_1: bool, decision_2: bool) -> None:
        """
        Increment both strategy's points according to the decisions.
        """
        if decision_1 is True and decision_2 is True:
            self._points[0] += REWARDS["collaboration"]
            self._points[1] += REWARDS["collaboration"]
        elif decision_1 is True and decision_2 is False:
            self._points[0] += REWARDS["failed_collaboration"]
            self._points[1] += REWARDS["successful_defection"]
        elif decision_1 is False and decision_2 is True:
            self._points[0] += REWARDS["successful_defection"]
            self._points[1] += REWARDS["failed_collaboration"]
        else:
            self._points[0] += REWARDS["defection"]
            self._points[1] += REWARDS["defection"]

    def _get_points_per_round(self) -> Tuple[float, float]:
        """
        Get the two points-per-round values
        """
        return (
            self._points[0] / self._rounds_count,
            self._points[1] / self._rounds_count,
        )
