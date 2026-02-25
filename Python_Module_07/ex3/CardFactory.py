from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):
    """
    Abstract base class defining a factory interface
    for creating cards and decks.

    Subclasses must implement methods to create different types of cards,
    generate themed decks, and report supported card types.
    This class follows the Factory design pattern for card creation.
    """
    @abstractmethod
    def create_creature(self, name_or_power) -> Card:
        """
        Create a creature-type card.

        Args:
            name_or_power: A parameter to define the creature's name or
                power level (implementation-dependent).

        Returns:
            Card: An instance of a CreatureCard or equivalent.
        """
        pass

    @abstractmethod
    def create_spell(self, name_or_power) -> Card:
        """
        Create a spell-type card.

        Args:
            name_or_power: A parameter to define the spell's name or effect
                (implementation-dependent).

        Returns:
            Card: An instance of a SpellCard or equivalent.
        """
        pass

    @abstractmethod
    def create_artifact(self, name_or_power) -> Card:
        """
        Create an artifact-type card.

        Args:
            name_or_power: A parameter to define the artifact's name or
                effect (implementation-dependent).

        Returns:
            Card: An instance of an ArtifactCard or equivalent.
        """
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        """
        Generate a themed deck containing a specified number of cards.

        Args:
            size (int): The number of cards to include in the deck.

        Returns:
            dict: A dictionary representing the deck, usually containing
            card objects and metadata about the deck.
        """
        pass

    @abstractmethod
    def get_supported_types(self) -> dict:
        """
        Retrieve the types of cards supported by this factory.

        Returns:
            dict: A dictionary mapping card type names to the corresponding
            creation methods or class references.
        """
        pass
