from prisoner.strategies.strategy import Strategy


class Defector(Strategy):
    """
    Simple strategy that always defects
    """
    def __init__(self):
        super().__init__("Defector")

    def decide_step(self, self_history: list, opponent_history: list) -> bool:
        """
        Always defects
        """
        return False
