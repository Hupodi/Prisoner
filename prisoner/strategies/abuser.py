from enum import Enum

from prisoner.strategies.strategy import Strategy


class StrategyState(Enum):
    """
    Enum for the different states of the abuser strategy
    """
    INIT = "INIT"
    TESTING = "TESTING"
    COLLABORATING = "COLLABORATING"
    ABUSING = "ABUSING"
    DEFENSIVE = "DEFENSIVE"


class Abuser(Strategy):
    """
    Strategy that:
    - Starts by collaborating for the first 3 rounds
    - At any points, if the opponent defected for 5 rounds in a row, will enter and endless defection loop
    -
    """

    def __init__(self):
        super().__init__("Abuser")
        self.state = StrategyState.INIT

    def decide_step(self, self_history: list, opponent_history: list) -> bool:
        """
        According to the strategy described above
        """
        decision = self.decide(opponent_history)
        self.update_state(opponent_history)
        return decision

    def decide(self, opponent_history: list) -> bool:
        """
        Decide for a single round.
        """
        match self.state:
            case StrategyState.INIT:
                return True
            case StrategyState.TESTING:
                return not opponent_history[-1]
            case StrategyState.ABUSING:
                return False
            case StrategyState.COLLABORATING:
                return True
            case StrategyState.DEFENSIVE:
                return False

    def update_state(self, opponent_history) -> None:
        """
        Update current strategy state
        """
        match self.state:

            case StrategyState.INIT:
                if len(opponent_history) <= 2:
                    return
                self.state = StrategyState.TESTING

            case StrategyState.TESTING:
                if len(opponent_history) <= 4:
                    return
                if sum(opponent_history[-3:]) == 3:
                    self.state = StrategyState.ABUSING
                elif sum(opponent_history[-3:]) <= 1:
                    self.state = StrategyState.DEFENSIVE
                else:
                    self.state = StrategyState.COLLABORATING

            case StrategyState.ABUSING:
                return

            case StrategyState.COLLABORATING:
                if sum(opponent_history[-3:]) <= 1:
                    self.state = StrategyState.DEFENSIVE

            case StrategyState.DEFENSIVE:
                return
