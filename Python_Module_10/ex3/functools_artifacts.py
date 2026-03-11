#!/usr/bin/env python3

import operator
import functools


def spell_reducer(spells: list[int], operation: str) -> int:
    """
    Reduce a list of spell power values using a specified operation.

    This function applies a reduction operation to the list of integers
    representing spell powers. Supported operations include addition,
    multiplication, maximum, and minimum.

    Args:
        spells (list[int]): A list of integer values representing spell powers.
        operation (str): The reduction operation to apply. Supported values
            are "add", "multiply", "max", and "min".

    Returns:
        int: The result of applying the chosen reduction operation
        to the list of spell powers.

    Raises:
        ValueError: If the specified operation is not supported.
    """
    if operation == "add":
        return functools.reduce(operator.add, spells)

    elif operation == "multiply":
        return functools.reduce(operator.mul, spells)

    elif operation == "max":
        return functools.reduce(max, spells)

    elif operation == "min":
        return functools.reduce(min, spells)

    else:
        raise ValueError(f"Operation {operation} not supported")


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    """
    Create specialized enchantment functions using partial application.

    This function generates predefined enchantment functions by fixing
    certain arguments of a base enchantment function using functools.partial.

    Args:
        base_enchantment (callable): A function that performs an enchantment,
        expected to accept parameters such as power and element type.

    Returns:
        dict[str, callable]: A dictionary containing specialized enchantment
        functions for fire, ice, and lightning.
    """
    return {
        'fire_enchant': functools.partial(base_enchantment, 50, 'fire'),
        'ice_enchant': functools.partial(base_enchantment, 50, 'ice'),
        'lightning_enchant': functools.partial(base_enchantment, 50,
                                               'lightning')
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """
    Compute the nth Fibonacci number using memoization.

    This function uses the functools.lru_cache decorator to store
    previously computed results, significantly improving performance
    for recursive calls.

    Args:
        n (int): The position in the Fibonacci sequence.

    Returns:
        int: The Fibonacci number at position n.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    """
    Create a spell dispatcher using single dispatch.

    The returned function dynamically selects the appropriate
    spell behavior depending on the type of argument passed.

    Supported argument types include integers, strings, and lists.

    Returns:
        callable: A dispatcher function that executes different
        logic depending on the input argument type.
    """

    @functools.singledispatch
    def cast_spell(arg):
        return "Unknown spell type"

    @cast_spell.register(int)
    def handle_integer(arg):
        return f"Deals {arg} damage"

    @cast_spell.register(str)
    def handle_string(arg):
        return f"Casts {arg} enchantment"

    @cast_spell.register(list)
    def handle_list(arg):
        return f"Multi-casting {len(arg)} spells"

    return cast_spell


def main():
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]

    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("Testing memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")


if __name__ == "__main__":
    main()
