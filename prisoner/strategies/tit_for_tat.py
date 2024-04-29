from prisoner.strategies.strategy import Strategy


class TitForTat(Strategy):
    """
    Simple strategy that plays what the opponent just played.
    """

    def __init__(self):
        super().__init__("Tit for Tat")

    def decide_step(self, self_history: list, opponent_history: list) -> bool:
        """
        Return the last move from the opponent
        """
        if len(opponent_history) == 0:
            return True

        return opponent_history[-1]
