from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck

def main():
    print("=== DataDeck Deck Builder ===")
    print("Building deck with different card types...")
    deck = Deck()
    spell = SpellCard("Lightning Bolt", 3, "Common", "Deal 3 damage to target")
    artifact = ArtifactCard("Mana Crystal", 2, "Rare", 5, "Permanent: +1 mana per turn")
    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    deck.add_card(spell)
    deck.add_card(artifact)
    deck.add_card(creature)
    print(f"Deck stats: {deck.get_deck_stats()}")
    print("Drawing and playing cards:")
    card1 = deck.draw_card()
    print(f"Drew: {card1.name} (Spell)")
    print(f"Play result: {card1.play({})}")
    card2 = deck.draw_card()
    print(f"Drew: {card2.name} (Artifact)")
    print(f"Play result: {card2.play({})}")
    card3 = deck.draw_card()
    print(f"Drew: {card3.name} (Creature)")
    print(f"Play result: {card3.play({})}")
    print("Polymorphism in action: Same interface, different card behaviors!")

if __name__ == "__main__":
    main()