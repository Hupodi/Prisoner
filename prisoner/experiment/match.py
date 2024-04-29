from typing import Tuple

import numpy as np
import plotly.graph_objects as go

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
        decision_2 = self._strategy_2.decide_step(
            self_history=self._history[1], opponent_history=self._history[0]
        )
        self._history[0].append(decision_1)
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

    def plot(self) -> go.Figure:
        """
        Basic Representation of a match as a plotly graph
        """
        x_range = np.arange(1, self._rounds_count + 1)
        fig = go.Figure(
            data=[
                go.Bar(
                    name=self._strategy_1.name,
                    x=x_range,
                    y=[0.5] * self._rounds_count,
                    marker_color=[
                        "lightgreen" if decision is True else "crimson"
                        for decision in self._history[0]
                    ],
                ),
                go.Bar(
                    name=self._strategy_2.name,
                    x=x_range,
                    y=[0.5] * self._rounds_count,
                    marker_color=[
                        "lightgreen" if decision is True else "crimson"
                        for decision in self._history[1]
                    ],
                ),
            ]
        )
        fig.update_layout(
            title_text=f"Match: {self._strategy_1.name} ({self._get_points_per_round()[0]}), {self._strategy_2.name} ({self._get_points_per_round()[1]})",
            xaxis={"title": "Round"},
            yaxis={
                "title": "",
                "tickvals": [0.25, 0.75],
                "ticktext": [self._strategy_1.name, self._strategy_2.name],
            },
            barmode="stack",
            showlegend=False,
        )
        return fig
