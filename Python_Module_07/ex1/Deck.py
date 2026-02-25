import random

from ex0.Card import Card


class Deck():
    """
    Represents a deck of cards in the game.

    The Deck class manages a collection of Card objects, allowing cards
    to be added, removed, shuffled, drawn, and analyzed for statistics.

    Attributes:
        cards (list[Card]): A list containing the cards currently in the deck.
    """

    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        """
        Add a card to the deck.

        Args:
            card (Card): The card instance to add to the deck.

        Returns:
            None
        """
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """
        Remove a card from the deck by its name.

        Args:
            card_name (str): The name of the card to remove.

        Returns:
            bool: True if the card was found and removed, otherwise False.
        """
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        """
        Shuffle the cards in the deck randomly.

        Returns:
            None
        """
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """
        Draw the top card from the deck.

        The top card is considered to be the first element in the list.

        Returns:
            Card: The drawn card if the deck is not empty.
            None: If the deck is empty.
        """
        if self.cards:
            return self.cards.pop(0)
        return None

    def get_deck_stats(self) -> dict:
        """
        Calculate statistical information about the deck.

        The method counts the number of cards by type (CreatureCard,
        SpellCard, ArtifactCard) and computes the average mana cost.

        Returns:
            dict: A dictionary containing:
                - total_cards (int): Total number of cards in the deck.
                - creatures (int): Number of CreatureCard instances.
                - spells (int): Number of SpellCard instances.
                - artifacts (int): Number of ArtifactCard instances.
                - avg_cost (float): Average cost of all cards in the deck.
        """
        creatures = 0
        spells = 0
        artifacts = 0
        total_cost = 0

        for card in self.cards:
            total_cost += card.cost
            class_name = card.__class__.__name__
            if class_name == 'CreatureCard':
                creatures += 1
            elif class_name == 'SpellCard':
                spells += 1
            elif class_name == 'ArtifactCard':
                artifacts += 1

        total = len(self.cards)
        if (total > 0):
            avg_cost = total_cost / total
        else:
            avg_cost = 0.0

        return {
            'total_cards': total,
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': avg_cost
        }
