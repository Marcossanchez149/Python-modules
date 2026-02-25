from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """
    Abstract base class defining the interface for a game-playing strategy.

    Subclasses must implement methods for executing a turn, retrieving the
    strategy name, and prioritizing targets. This allows different AI or
    player behaviors to be plugged into the GameEngine.
    """

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """
        Execute a turn based on the current hand and battlefield state.

        Args:
            hand (list): A list of card objects currently in the player's hand.
            battlefield (list): A list of cards or entities on the battlefield.

        Returns:
            dict: A dictionary summarizing the actions taken during the turn,
            such as cards played, mana used, targets attacked,
            and damage dealt.
        """
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """
        Retrieve the name of the strategy.

        Returns:
            str: The name of the strategy implementation.
        """
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """
        Determine the order of targets for attacks or abilities.

        Args:
            available_targets (list): A list of possible targets.

        Returns:
            list: A reordered list of targets according to
            the strategy's priorities.
        """
        pass
