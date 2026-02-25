from abc import ABC, abstractmethod


class Magical(ABC):
    """
    Abstract base class that defines magical abilities.

    Any class that inherits from Magical must implement methods
    related to spell casting, mana manipulation, and retrieval
    of magical statistics. This interface ensures a consistent
    contract for magic-capable entities within the game system.
    """

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """
        Cast a spell on one or more targets.

        Args:
            spell_name (str): The name of the spell being cast.
            targets (list): A list of targets affected by the spell.

        Returns:
            dict: A dictionary describing the outcome of the spell,
            such as mana usage and affected targets.
        """
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """
        Increase or restore mana.

        Args:
            amount (int): The amount of mana to add to the current pool.

        Returns:
            dict: A dictionary containing details about the mana
            change and the updated mana total.
        """
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """
        Retrieve magical statistics of the entity.

        Returns:
            dict: A dictionary containing magic-related attributes,
            such as current mana or spell power.
        """
        pass
