from ex0.Card import Card


class SpellCard(Card):
    """
    Represents a spell-type card in the game.

    A SpellCard is a playable card that produces an immediate effect
    when cast. Unlike creatures or artifacts, spells typically resolve
    their effect and do not remain on the battlefield.

    Attributes:
        name (str): The name of the card.
        cost (int): The mana or resource cost required to cast the spell.
        rarity (str): The rarity level of the card.
        effect_type (str): A description of the spell's effect.
    """

    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        self.effect_type = effect_type
        super().__init__(name, cost, rarity)

    def play(self, game_state: dict) -> dict:
        """
        Cast the spell and apply its primary effect.

        Args:
            game_state (dict): A dictionary representing
            the current game state.

        Returns:
            dict: A dictionary describing the result of casting the spell,
            including mana usage and the spell's effect.
        """
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.effect_type
        }

    def resolve_effect(self, targets: list) -> dict:
        """
        Resolve the spell's effect on the specified targets.

        Args:
            targets (list): A list of targets affected by the spell.

        Returns:
            dict: A dictionary indicating the spell name and the number
            of targets that were affected.
        """
        return {
            'spell': self.name,
            'targets_resolved': len(targets)
        }

    def get_card_info(self) -> dict:
        """
        Retrieve detailed information about the spell card.

        Returns:
            dict: A dictionary containing the base card information plus
            spell-specific attributes such as type and effect type.
        """
        info = super().get_card_info()
        info['type'] = 'Spell'
        info['effect_type'] = self.effect_type
        return info
