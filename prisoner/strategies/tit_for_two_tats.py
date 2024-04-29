from prisoner.strategies.strategy import Strategy


class TitForTwoTats(Strategy):
    """
    Strategy that defects if for the past 2 steps the opponent defected.
    """
    def __init__(self):
        super().__init__("Tit for Two Tat")

    def decide_step(self, self_history: list, opponent_history: list) -> bool:
        """
        Defects if for the past 2 steps the opponent defected.
        """
        if len(opponent_history) <= 1:
            return True

        return not(opponent_history[-2] is False and opponent_history[-1] is False)
