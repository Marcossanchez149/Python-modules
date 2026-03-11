#!/usr/bin/env python3

import time
import functools


def spell_timer(func: callable) -> callable:
    """
    Decorator that measures and prints the execution time of a spell function.

    This decorator prints a message before the function execution, records the
    start and end time, and displays how long the spell took to execute.

    Args:
        func (callable): The function representing the spell to be timed.

    Returns:
        callable: The wrapped function that includes timing functionality.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    """
    Decorator factory that validates whether a spell
    has enough power to be cast.

    The decorator checks if the provided power level meets the minimum required
    power. The power value is searched in keyword arguments first and then in
    positional arguments.

    Args:
        min_power (int): The minimum power required to execute the spell.

    Returns:
        callable: A decorator that validates the power level
        before calling the function.
    """

    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            power_level = kwargs.get('power')
            if power_level is None:
                for arg in args:
                    if isinstance(arg, int):
                        power_level = arg
                        break
            if power_level is None or power_level < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> callable:
    """
    Decorator factory that retries a spell if it raises an exception.

    The decorated function will be executed multiple times until it succeeds
    or the maximum number of attempts is reached.

    Args:
        max_attempts (int): The maximum number of retry attempts.

    Returns:
        callable: A decorator that adds retry logic to the function.
    """

    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper

    return decorator


class MageGuild:
    """
    Represents a guild of mages capable of validating mage names
    and casting spells with power restrictions.
    """

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """
        Validate a mage's name.

        The name must contain at least three characters and may only
        include alphabetic characters and spaces.

        Args:
            name (str): The mage's name.

        Returns:
            bool: True if the name is valid, False otherwise.
        """
        if len(name) < 3:
            return False
        for char in name:
            if not char.isalpha() and not char.isspace():
                return False
        return True

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """
        Cast a spell with a given power level.

        The method is decorated with a power validator that ensures the
        provided power meets the minimum required value.

        Args:
            spell_name (str): The name of the spell to cast.
            power (int): The power level used to cast the spell.

        Returns:
            str: A message indicating the result of the spell casting.
        """
        return f"Successfully cast {spell_name} with power {power}"


def main():
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"
    print(f"Result: {fireball()}")
    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf the White"))
    print(MageGuild.validate_mage_name("X"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))


if __name__ == "__main__":
    main()
