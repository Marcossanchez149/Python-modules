#!/usr/bin/env python3

def spell_combiner(spell1: callable, spell2: callable) -> callable:
    """
    Combine two spell functions into a single callable.

    The resulting function will apply both spells to the same target
    and return their results as a tuple.

    Args:
        spell1 (callable): The first spell function that accepts a target.
        spell2 (callable): The second spell function that accepts a target.

    Returns:
        callable: A function that takes a target and returns a tuple
        containing the results of both spells.
    """
    def combined_spell(target):
        return (spell1(target), spell2(target))
    return combined_spell


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """
    Amplify the effect of a base spell by multiplying its result.

    The returned function calls the original spell and multiplies
    its numeric output by the given multiplier.

    Args:
        base_spell (callable): A function that returns a numeric value.
        multiplier (int): The factor used to amplify the spell's power.

    Returns:
        callable: A new function that returns the amplified result.
    """
    def amplified_spell():
        return base_spell() * multiplier
    return amplified_spell


def conditional_caster(condition: callable, spell: callable) -> callable:
    """
    Create a spell that is only cast if a given condition is met.

    The returned function checks the condition on the target before
    casting the spell. If the condition is not satisfied, the spell
    fails with a message.

    Args:
        condition (callable): A function that takes a target and
            returns a boolean indicating whether the spell can be cast.
        spell (callable): A function representing the spell to cast.

    Returns:
        callable: A function that attempts to cast the spell on a target.
    """

    def cast_if_true(target):
        if condition(target):
            return spell(target)
        return "Spell fizzled"

    return cast_if_true


def spell_sequence(spells: list[callable]) -> callable:
    """
    Create a function that casts multiple spells in sequence.

    Each spell in the list is applied to the same target, and the
    results are collected into a list.

    Args:
        spells (list[callable]): A list of spell functions that each
            accept a target as input.

    Returns:
        callable: A function that takes a target and returns a list
        containing the results of each spell.
    """

    def cast_all(target):
        return [spell(target) for spell in spells]
    return cast_all


def main():

    def fireball(target):
        return f"Fireball hits {target}"

    def heal(target):
        return f"Heals {target}"

    def damage():
        return 10

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    res1, res2 = combined("Dragon")
    print(f"Combined spell result: {res1}, {res2}")

    print("\nTesting power amplifier...")
    mega_damage = power_amplifier(damage, 3)
    print(f"Original: {damage()}, Amplified: {mega_damage()}")


if __name__ == "__main__":
    main()
