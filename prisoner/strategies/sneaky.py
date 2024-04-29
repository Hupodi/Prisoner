from prisoner.strategies.strategy import Strategy


class Sneaky(Strategy):
    """
    Strategy that defects if for the past 2 steps the opponent collaborated.
    """
    def __init__(self):
        super().__init__("Sneaky")

    def decide_step(self, self_history: list, opponent_history: list) -> bool:
        """
        Defects if for the past 2 steps the opponent collaborated.
        """
        if len(opponent_history) <= 1:
            return True

        return opponent_history[-2] is False or opponent_history[-1] is False
