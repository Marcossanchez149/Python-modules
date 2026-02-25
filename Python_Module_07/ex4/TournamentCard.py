from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """
    Represents a card used in tournament-style competitive gameplay.

    TournamentCard combines combat abilities and ranking capabilities,
    allowing it to participate in battles, track performance, and maintain
    a rating and win/loss record.

    Attributes:
        name (str): The name of the card.
        cost (int): The mana or resource cost to play the card.
        rarity (str): The rarity level of the card.
        attack_val (int): The attack value used in combat.
        defense_val (int): The defense value used to mitigate damage.
        card_id (str): A unique identifier for the tournament card.
        rating (int): The current rating of the card.
        wins (int): Total number of wins.
        losses (int): Total number of losses.
    """
    def __init__(self, name: str, cost: int, rarity: str,
                 attack_val: int, defense_val: int, card_id: str,
                 initial_rating: int):
        super().__init__(name, cost, rarity)
        self.attack_val = attack_val
        self.defense_val = defense_val
        self.card_id = card_id
        self.rating = initial_rating
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        """
        Play the card in a tournament context.

        Args:
            game_state (dict): Current state of the game (unused here).

        Returns:
            dict: A dictionary indicating that the card has been played.
        """
        return {'card': self.name, 'action': 'played in tournament'}

    def attack(self, target) -> dict:
        """
        Perform an attack against a target.

        Args:
            target: The entity being attacked.

        Returns:
            dict: A dictionary describing the attack, including attacker,
            target, and damage dealt.
        """
        return {'attacker': self.name, 'target': target,
                'damage': self.attack_val}

    def defend(self, incoming_damage: int) -> dict:
        """
        Defend against incoming damage.

        Args:
            incoming_damage (int): The amount of damage received.

        Returns:
            dict: A dictionary describing the damage taken.
        """
        return {'defender': self.name, 'damage_taken': incoming_damage}

    def get_combat_stats(self) -> dict:
        """
        Retrieve the card's combat statistics.

        Returns:
            dict: A dictionary containing attack and defense values.
        """
        return {'attack': self.attack_val, 'defense': self.defense_val}

    def calculate_rating(self) -> int:
        """
        Calculate the current rating of the card.

        Returns:
            int: The card's current rating.
        """
        return self.rating

    def update_wins(self, wins: int) -> None:
        """
        Increment the card's win count.

        Args:
            wins (int): Number of wins to add.

        Returns:
            None
        """
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        """
        Increment the card's loss count.

        Args:
            losses (int): Number of losses to add.

        Returns:
            None
        """
        self.losses += losses

    def get_rank_info(self) -> dict:
        """
        Retrieve ranking information.

        Returns:
            dict: A dictionary containing rating, wins, and losses.
        """
        return {'rating': self.rating, 'wins': self.wins,
                'losses': self.losses}

    def get_tournament_stats(self) -> dict:
        """
        Retrieve detailed tournament statistics for the card.

        Returns:
            dict: A dictionary containing card ID, name, rating,
            and win-loss record.
        """
        return {
            'id': self.card_id,
            'name': self.name,
            'rating': self.rating,
            'record': f"{self.wins}-{self.losses}"
        }
