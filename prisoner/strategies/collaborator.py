from prisoner.strategies.strategy import Strategy


class Collaborator(Strategy):
    """
    Simple strategy that always collaborates
    """

    def decide_step(self, self_history: list, opponent_history: list) -> bool:
        """
        Always collaborate
        """
        return True
