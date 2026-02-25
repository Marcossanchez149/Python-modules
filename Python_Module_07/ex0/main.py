#!/usr/bin/env python3
from .CreatureCard import CreatureCard


def main():
    print("=== DataDeck Card Foundation ===")
    print("Testing Abstract Base Class Design:")
    try:
        dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        print("CreatureCard Info:")
        print(dragon.get_card_info())
        print("Playing Fire Dragon with 6 mana available:")
        print(f"Playable: {dragon.is_playable(6)}")
        print(f"Play result: {dragon.play({})}")
        print("Fire Dragon attacks Goblin Warrior:")
        print(f"Attack result: {dragon.attack_target('Goblin Warrior')}")
        print("Testing insufficient mana (3 available):")
        print(f"Playable: {dragon.is_playable(3)}")
        print("Abstract pattern successfully demonstrated!")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
