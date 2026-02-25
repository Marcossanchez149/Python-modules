from abc import ABC, abstractmethod


class Combatable(ABC):
    """
    Abstract base class that defines combat-related behavior.

    Any class that inherits from Combatable must implement the
    required combat methods, enabling interaction in a combat system
    such as attacking, defending, and reporting combat statistics.
    """

    @abstractmethod
    def attack(self, target) -> dict:
        """
        Perform an attack against a specified target.

        Args:
            target: The entity being attacked. The exact type depends
                on the implementation (e.g., another creature or player).

        Returns:
            dict: A dictionary describing the outcome of the attack,
            such as damage dealt or combat resolution details.
        """
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """
        Defend against incoming damage.

        Args:
            incoming_damage (int): The amount of damage received
                from an attack.

        Returns:
            dict: A dictionary describing the result of the defense,
            such as remaining health or damage mitigated.
        """
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """
        Retrieve the combat-related statistics of the entity.

        Returns:
            dict: A dictionary containing combat attributes such as
            attack power, health, defense, or other relevant stats.
        """
        pass
