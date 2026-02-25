from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===")
    print("Registering Tournament Cards...")
    platform = TournamentPlatform()
    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5,
                            "dragon_001", 1200)
    wizard = TournamentCard("Ice Wizard", 4, "Epic", 5, 4, "wizard_001", 1150)
    platform.register_card(dragon)
    platform.register_card(wizard)
    for card in [dragon, wizard]:
        print(f"{card.name} (ID: {card.card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.wins}-{card.losses}")
    print("Creating tournament match...")
    match_result = platform.create_match("dragon_001", "wizard_001")
    print(f"Match result: {match_result}")
    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, entry in enumerate(leaderboard, 1):
        print(f"{i}. {entry}")
    print("Platform Report:")
    print(platform.generate_tournament_report())
    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
