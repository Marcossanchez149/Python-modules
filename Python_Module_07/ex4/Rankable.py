from abc import ABC, abstractmethod


class Rankable(ABC):
    """
    Abstract base class for entities that can be ranked or rated.

    Subclasses must implement methods for calculating a rating,
    updating wins and losses, and retrieving ranking information.
    This interface is useful for leaderboard or competitive tracking
    systems within a game.
    """

    @abstractmethod
    def calculate_rating(self) -> int:
        """
        Calculate the current rating of the entity.

        Returns:
            int: The computed rating value, based on wins, losses,
            or other performance metrics.
        """
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """
        Update the entity's record with additional wins.

        Args:
            wins (int): The number of wins to add.

        Returns:
            None
        """
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """
        Update the entity's record with additional losses.

        Args:
            losses (int): The number of losses to add.

        Returns:
            None
        """
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """
        Retrieve ranking information for the entity.

        Returns:
            dict: A dictionary containing rank-related data,
            such as current rating, total wins, total losses, etc.
        """
        pass
