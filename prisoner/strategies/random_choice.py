import random

from prisoner.strategies.strategy import Strategy


class RandomChoice(Strategy):
    """
    Simple strategy that always collaborates
    """

    def __init__(self, collaborate_probability: float) -> None:
        """
        Init: store collaborate_probability
        """
        super().__init__(f"Random, collaborate Proba = {collaborate_probability}")
        self._collaborate_probability = collaborate_probability

    def decide_step(self, self_history: list, opponent_history: list) -> bool:
        """
        Always collaborate
        """
        return random.choices(
            [True, False],
            [self._collaborate_probability, 1 - self._collaborate_probability],
        )[0]
