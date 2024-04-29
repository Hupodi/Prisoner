"""
Main caller for a Prisonner's Dilemma contest of strategies.
"""

from prisoner.strategies import (
    Collaborator,
    Defector,
    RandomChoice,
    TitForTat,
    Triggerable,
    TitForTwoTats,
    Sneaky,
)
from prisoner.experiment.contest import Contest


def play_contest():
    """
    Play the contest:
        - Initialise all strategies
        - Play the full contest: all matches, compute all points
        - Observe results
    """
    strategies = [
        Collaborator(),
        Defector(),
        RandomChoice(collaborate_probability=0.5),
        RandomChoice(collaborate_probability=0.2),
        RandomChoice(collaborate_probability=0.8),
        TitForTat(),
        Triggerable(),
        TitForTwoTats(),
        Sneaky(),
    ]
    contest = Contest(strategies=strategies)
    contest.play_contest()
    print(contest)


if __name__ == "__main__":
    play_contest()
