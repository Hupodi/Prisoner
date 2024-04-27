from abc import ABC, abstractmethod


class Strategy(ABC):
    """
    Abstract base class representing a strategy
    """

    @abstractmethod
    def decide_step(self) -> bool:
        """
        Get the next step decision for the strategy.
        """
        pass
