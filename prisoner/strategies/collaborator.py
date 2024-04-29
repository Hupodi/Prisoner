from prisoner.strategies.strategy import Strategy


class Collaborator(Strategy):
    """
    Simple strategy that always collaborates
    """

    def __init__(self):
        super().__init__("Collaborator")

    def decide_step(self, self_history: list, opponent_history: list) -> bool:
        """
        Always collaborate
        """
        return True
