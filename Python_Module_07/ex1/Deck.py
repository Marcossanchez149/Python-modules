import random

from ex0.Card import Card

class Deck():

    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                self.cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards:
            return self.cards.pop(0)
        return None

    def get_deck_stats(self) -> dict:
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
        if (total > 0) :
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
