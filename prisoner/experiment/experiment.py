class Match:
    """
    Class representing a prisoner's dilemma match between two strategies
    """
    def __init__(self, strategy_1, strategy_2, rounds_count: int = 200):
        self._scores = {}
