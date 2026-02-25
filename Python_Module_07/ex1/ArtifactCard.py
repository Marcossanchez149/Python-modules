from ex0.Card import Card


class ArtifactCard(Card):
    """
    Represents an artifact-type card in the game.

    An ArtifactCard is a playable card that provides a persistent effect
    and may have an activatable ability. Artifacts typically remain in play
    and can be used multiple times depending on their durability.

    Attributes:
        name (str): The name of the card.
        cost (int): The mana or resource cost required to play the card.
        rarity (str): The rarity level of the card.
        durability (int): The number of times the artifact can be used
            before being destroyed or removed.
        effect (str): A description of the artifact's effect when played.
    """
    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str) -> None:
        self.durability = durability
        self.effect = effect
        super().__init__(name, cost, rarity)

    def play(self, game_state: dict) -> dict:
        """
        Play the artifact card and apply its effect.

        Args:
            game_state (dict): A dictionary representing
             the current game state.

        Returns:
            dict: A dictionary describing the result of playing the card,
            including mana usage and the artifact's effect.
        """
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect
        }

    def activate_ability(self) -> dict:
        """
        Activate the artifact's special ability.

        Returns:
            dict: A dictionary indicating that the artifact's ability
            has been activated.
        """
        return {
            'artifact': self.name,
            'ability_activated': True
        }

    def get_card_info(self) -> dict:
        """
        Retrieve detailed information about the artifact card.

        Returns:
            dict: A dictionary containing the base card information plus
            artifact-specific attributes such as type, durability, and effect.
        """
        info = super().get_card_info()
        info['type'] = 'Artifact'
        info['durability'] = self.durability
        info['effect'] = self.effect
        return info
