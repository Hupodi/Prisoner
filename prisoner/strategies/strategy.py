from abc import ABC, abstractmethod


class Strategy(ABC):
    """
    Abstract base class representing a strategy
    """

    def __init__(self, name: str) -> None:
        """
        Add strategy name
        """
        self.name = name

    @abstractmethod
    def decide_step(self, self_history: list, opponent_history: list) -> bool:
        """
        Get the next step decision for the strategy. Returns True for collaboration, False for defection.
        """
        pass
