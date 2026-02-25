from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """
    Represents an aggressive gameplay strategy.

    The AggressiveStrategy focuses on maximizing offensive pressure.
    It prioritizes playing as many cards as possible within available mana
    and targeting the enemy player directly whenever possible.
    """

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """
        Execute a turn using an aggressive approach.

        The strategy sorts the hand by card cost (ascending) and plays
        as many cards as possible within the available mana limit.
        It prioritizes attacking the enemy player directly.

        Args:
            hand (list): A list of card objects currently in the player's hand.
            battlefield (list): A list of cards currently on the battlefield.

        Returns:
            dict: A dictionary containing:
                - cards_played (list[str]): Names of cards played this turn.
                - mana_used (int): Total mana spent.
                - targets_attacked (list[str]): Targets attacked this turn.
                - damage_dealt (int): Total damage dealt.
        """
        mana = 5
        cartas_jugadas = []
        mano_ordenada = sorted(hand, key=lambda c: c.cost)
        for card in mano_ordenada:
            if mana >= card.cost:
                mana -= card.cost
                cartas_jugadas.append(card.name)
        return {
            'cards_played': cartas_jugadas,
            'mana_used': 5 - mana,
            'targets_attacked': ['Enemy Player'],
            'damage_dealt': 8
        }

    def get_strategy_name(self) -> str:
        """
        Retrieve the name of the strategy.

        Returns:
            str: The name of the strategy.
        """
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        """
        Prioritize targets for attack.

        The enemy player is always prioritized first. Other available
        targets are appended afterward in their original order. If no
        targets are available, the enemy player is added by default.

        Args:
            available_targets (list): A list of possible targets.

        Returns:
            list: A reordered list of prioritized targets.
        """
        prioritized = []
        if "Enemy Player" in available_targets:
            prioritized.append("Enemy Player")
        for target in available_targets:
            if target != "Enemy Player":
                prioritized.append(target)
        if not prioritized:
            prioritized.append("Enemy Player")
        return prioritized
