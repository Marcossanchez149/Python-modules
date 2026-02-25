from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:
    """
    Core engine for simulating a card game.

    The GameEngine manages card creation, executes strategy-driven turns,
    and tracks game statistics such as total damage, cards created, and turns
    simulated. It uses a CardFactory to generate cards and a GameStrategy
    to determine actions during each turn.
    """
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """
        Configure the game engine with a card factory and a strategy.

        Args:
            factory (CardFactory): A factory instance for creating cards.
            strategy (GameStrategy): A strategy instance defining turn actions.

        Returns:
            None
        """
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        """
        Simulate a single turn of the game.

        The method generates a hand of cards using the configured factory,
        executes the strategy for this turn, updates statistics, and returns
        the results.

        Returns:
            dict: A dictionary containing the results of the turn, including
            cards played, mana used, targets attacked, and damage dealt.
        """
        self.turns_simulated += 1
        hand = [
            self.factory.create_creature("dragon"),
            self.factory.create_creature("goblin"),
            self.factory.create_spell("lightning")
        ]
        self.cards_created += len(hand)
        turn_results = self.strategy.execute_turn(hand, [])
        self.total_damage += turn_results.get('damage_dealt', 0)
        return turn_results

    def get_engine_status(self) -> dict:
        """
        Retrieve the current status and statistics of the game engine.

        Returns:
            dict: A dictionary containing:
                - turns_simulated (int): Number of turns simulated so far.
                - strategy_used (str): Name of the strategy
                currently configured.
                - total_damage (int): Total damage dealt across all turns.
                - cards_created (int): Total number of cards created.
        """
        if self.strategy:
            strate = self.strategy.get_strategy_name()
        else:
            strate = "None"
        return {
            'turns_simulated': self.turns_simulated,
            'strategy_used': strate,
            'total_damage': self.total_damage,
            'cards_created': self.cards_created
        }
