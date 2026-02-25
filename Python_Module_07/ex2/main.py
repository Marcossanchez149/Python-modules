#!/usr/bin/env python3

from ex2.EliteCard import EliteCard


def main():
    print("=== DataDeck Ability System ===")
    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")
    arcane_warrior = EliteCard("Arcane Warrior", 6, "Epic", attack_val=5,
                               defense_val=3, health=10, mana=8)
    print("Playing Arcane Warrior (Elite Card):")
    print("Combat phase:")
    print(f"Attack result: {arcane_warrior.attack('Enemy')}")
    print(f"Defense result: {arcane_warrior.defend(5)}")
    print("Magic phase:")
    print(f"Spell cast: "
          f"{arcane_warrior.cast_spell('Fireball',['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {arcane_warrior.channel_mana(3)}")
    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
