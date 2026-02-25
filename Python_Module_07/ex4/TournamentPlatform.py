from .TournamentCard import TournamentCard


class TournamentPlatform:
    """
    Platform to manage tournament-style gameplay for TournamentCards.

    TournamentPlatform handles card registration, match creation, rating
    updates, leaderboards, and overall tournament reporting.
    """
    def __init__(self):
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        """
        Register a card to the tournament platform.

        Args:
            card (TournamentCard): The card instance to register.

        Returns:
            str: The unique card ID assigned to the registered card.
        """
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """
        Simulate a match between two registered cards.

        The first card is treated as the winner, updating wins, losses,
        and rating points accordingly.

        Args:
            card1_id (str): The ID of the winning card.
            card2_id (str): The ID of the losing card.

        Returns:
            dict: A dictionary containing:
                - winner (str): Winner card ID.
                - loser (str): Loser card ID.
                - winner_rating (int): Updated rating of the winner.
                - loser_rating (int): Updated rating of the loser.
        """
        c1 = self.cards[card1_id]
        c2 = self.cards[card2_id]
        c1.update_wins(1)
        c2.update_losses(1)
        c1.rating += 16
        c2.rating -= 16
        self.matches_played += 1
        return {
            'winner': c1.card_id,
            'loser': c2.card_id,
            'winner_rating': c1.calculate_rating(),
            'loser_rating': c2.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        """
        Generate a leaderboard sorted by card rating.

        Returns:
            list: A list of strings describing each card in descending
            order of rating, including wins and losses.
        """
        sorted_cards = sorted(self.cards.values(), key=lambda c: c.rating,
                              reverse=True)
        return [f"{c.name} - Rating: {c.rating} ({c.wins}-{c.losses})"
                for c in sorted_cards]

    def generate_tournament_report(self) -> dict:
        """
        Generate a summary report for the tournament platform.

        Returns:
            dict: A dictionary containing:
                - total_cards (int): Total number of registered cards.
                - matches_played (int): Total number of matches conducted.
                - avg_rating (int): Average rating of all registered cards.
                - platform_status (str): Current status of the platform.
        """
        total = len(self.cards)
        avg = sum(c.rating for c
                  in self.cards.values()) // total if total > 0 else 0
        return {
            'total_cards': total,
            'matches_played': self.matches_played,
            'avg_rating': avg,
            'platform_status': 'active'
        }
