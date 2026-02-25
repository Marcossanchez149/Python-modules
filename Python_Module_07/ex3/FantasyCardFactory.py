from .CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    """
    Concrete implementation of CardFactory for a fantasy-themed card game.

    This factory creates fantasy-themed creatures, spells, and artifacts,
    and can also generate themed decks. Supported creatures include dragons
    and goblins, while spells and artifacts follow typical fantasy conventions.
    """
    def create_creature(self, name_or_power) -> Card:
        """
        Create a fantasy creature card based on the input.

        Args:
            name_or_power: A string representing the type
            of creature to create.

        Returns:
            Card: An instance of CreatureCard matching the requested type.
        """
        if name_or_power == "dragon":
            return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        elif name_or_power == "goblin":
            return CreatureCard("Goblin Warrior", 2, "Common", 3, 2)
        return CreatureCard("Unknown Creature", 1, "Common", 1, 1)

    def create_spell(self, name_or_power) -> Card:
        """
        Create a fantasy spell card based on the input.

        Args:
            name_or_power: A string representing the type of spell to create.

        Returns:
            Card: An instance of SpellCard matching the requested type.
        """
        if name_or_power == "lightning":
            return SpellCard("Lightning Bolt", 3, "Common", "Deal 3 "
                             "damage to target")
        elif name_or_power == "Ice":
            return SpellCard("Ice damage", 2, "Common", "Deal 2 "
                             "damage to target")
        return SpellCard("Fireball", 4, "Rare", "Deal 5 damage")

    def create_artifact(self, name_or_power) -> Card:
        """
        Create a fantasy artifact card.

        Args:
            name_or_power: A string representing the artifact's name.

        Returns:
            Card: An instance of ArtifactCard with
            predefined durability and effect.
        """
        return ArtifactCard(name_or_power, 2, "Rare", 5, "Permanent: +1 "
                                                         "mana per turn")

    def create_themed_deck(self, size: int) -> dict:
        """
        Generate a fantasy-themed deck.

        Args:
            size (int): The number of cards in the deck.

        Returns:
            dict: A dictionary describing the deck, including size and theme.
        """
        return {"deck_size": size, "theme": "Fantasy"}

    def get_supported_types(self) -> dict:
        """
        Retrieve the types of cards supported by this factory.

        Returns:
            dict: A dictionary mapping card categories to supported types.
        """
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball', 'Ice', 'lightning'],
            'artifacts': ['mana_ring']
        }
