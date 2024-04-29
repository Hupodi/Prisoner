from prisoner.strategies.strategy import Strategy


class Triggerable(Strategy):
    """
    Strategy that collaborates but after a single defection from the opponent, it will keep defecting as a reaction.
    """

    def __init__(self):
        super().__init__("Triggerable")

    def decide_step(self, self_history: list, opponent_history: list) -> bool:
        """
        Collaborates but after a single defection from the opponent, it will keep defecting endlessly.
        """
        if len(self_history) == 0:
            return True

        return self_history[-1] and opponent_history[-1]
