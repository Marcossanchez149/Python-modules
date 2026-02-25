from abc import ABC, abstractmethod


class Card(ABC):
    """
    Abstract base class representing a generic card in a card-based game.

    This class defines the common attributes and behaviors shared by all cards.
    Concrete card types must inherit from this class
    and implement the `play` method.

    Attributes:
        name (str): The name of the card.
        cost (int): The mana or resource cost required to play the card.
        rarity (str): The rarity level of the card (e.g., common, rare, epic).
    """

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict):
        """
        Execute the card's effect on the game state.

        This method must be implemented by all subclasses. It defines
        how the card interacts with and modifies the game state when played.

        Args:
            game_state (dict): A dictionary representing the current state
                of the game, which may include players,
                board state, scores, etc.

        Returns:
            None
        """
        pass

    def get_card_info(self) -> dict:
        """
        Retrieve basic information about the card.

        Returns:
            dict: A dictionary containing the card's name, cost, and rarity.
        """
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        """
        Determine whether the card can be played based on available mana.

        Args:
            available_mana (int): The amount of mana
            or resources currently available.

        Returns:
            bool: True if the available mana is greater than or equal to
            the card's cost, otherwise False.
        """
        if (available_mana >= self.cost):
            return True
        else:
            return False
