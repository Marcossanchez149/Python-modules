from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard (Card, Combatable, Magical):
    """
    Represents a powerful hybrid card with both combat and magical abilities.

    EliteCard extends Card and implements both Combatable and Magical
    interfaces, allowing it to engage in melee combat and cast spells.
    It combines physical attributes (attack, defense, health) with
    magical resources (mana).

    Attributes:
        name (str): The name of the card.
        cost (int): The mana or resource cost required to play the card.
        rarity (str): The rarity level of the card.
        attack_val (int): The physical attack value used in combat.
        defense_val (int): The defensive value used to mitigate damage.
        health (int): The current health of the card.
        mana (int): The current mana available for casting spells.
    """

    def __init__(self, name: str, cost: int, rarity: str, attack_val: int,
                 defense_val: int, health: int, mana: int):
        super().__init__(name, cost, rarity)
        self.attack_val = attack_val
        self.defense_val = defense_val
        self.health = health
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        """
        Play the elite card and deploy it to the battlefield.

        Args:
            game_state (dict): A dictionary representing
            the current game state.

        Returns:
            dict: A dictionary describing the result of playing the card.
        """
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Elite warrior deployed'
        }

    def attack(self, target) -> dict:
        """
        Perform a melee attack against a target.

        Args:
            target: The entity being attacked.

        Returns:
            dict: A dictionary describing the combat interaction,
            including damage dealt and combat type.
        """
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.attack_val,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> dict:
        """
        Defend against incoming damage using defensive value.

        Args:
            incoming_damage (int): The amount of damage received.

        Returns:
            dict: A dictionary describing damage taken, whether it was
            blocked, and whether the card is still alive.
        """
        blocked = False
        if (self.defense_val > incoming_damage):
            blocked = True
        taken = incoming_damage - blocked
        self.health -= taken
        return {
            'defender': self.name,
            'damage_taken': taken,
            'damage_blocked': blocked,
            'still_alive': self.health > 0
        }

    def get_combat_stats(self) -> dict:
        """
        Retrieve the current combat statistics.

        Returns:
            dict: A dictionary containing attack, defense, and health values.
        """
        return {
            'attack': self.attack_val,
            'defense': self.defense_val,
            'health': self.health
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """
        Cast a spell on specified targets.

        Args:
            spell_name (str): The name of the spell being cast.
            targets (list): A list of targets affected by the spell.

        Returns:
            dict: A dictionary describing the spell cast,
            including mana consumption and targets.
        """
        mana_used = 4
        self.mana -= mana_used
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': mana_used
        }

    def channel_mana(self, amount: int) -> dict:
        """
        Increase the card's available mana.

        Args:
            amount (int): The amount of mana to add.

        Returns:
            dict: A dictionary containing the amount channeled
            and the updated total mana.
        """
        self.mana += amount
        return {
            'channeled': amount,
            'total_mana': self.mana
        }

    def get_magic_stats(self) -> dict:
        """
        Retrieve the current magical statistics.

        Returns:
            dict: A dictionary containing the current mana value.
        """
        return {'mana': self.mana}
