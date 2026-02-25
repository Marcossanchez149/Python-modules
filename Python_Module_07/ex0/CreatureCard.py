from .Card import Card


class CreatureCard(Card):
    """
    Represents a creature-type card in the game.

    A CreatureCard is a playable card that has combat attributes such as
    attack and health. When played, it is summoned to the battlefield
    and can interact with other entities through combat.

    Attributes:
        name (str): The name of the card.
        cost (int): The mana or resource cost required to play the card.
        rarity (str): The rarity level of the card.
        attack (int): The attack value representing the damage dealt in combat.
        health (int): The health value representing the creature's durability.
    """

    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack must be a positive integer.")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive integer.")
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        """
        Play the creature card and summon it to the battlefield.

        Args:
            game_state (dict): A dictionary representing
            the current game state.

        Returns:
            dict: A dictionary describing the result of playing the card,
            including mana usage and the summoning effect.
        """
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
        }

    def get_card_info(self) -> dict:
        """
        Retrieve detailed information about the creature card.

        Returns:
            dict: A dictionary containing the base card information plus
            creature-specific attributes such as type, attack, and health.
        """
        info = super().get_card_info()
        info['type'] = 'Creature'
        info['attack'] = self.attack
        info['health'] = self.health
        return info

    def attack_target(self, target) -> dict:
        """
        Perform an attack against a specified target.

        Args:
            target: The target of the attack
            (e.g., another creature or player).

        Returns:
            dict: A dictionary describing the combat interaction,
            including attacker name, target, damage dealt
            and resolution status.
        """
        target_name = target
        return {
            'attacker': self.name,
            'target': target_name,
            'damage_dealt': self.attack,
            'combat_resolved': True
        }
