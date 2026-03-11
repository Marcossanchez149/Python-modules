#!/usr/bin/env python3

def mage_counter() -> callable:
    """
    Create a counter function that tracks how many times it has been called.

    The returned function keeps an internal count using a closure and
    increments the count each time it is invoked.

    Returns:
        callable: A function that returns the current count after
        incrementing it by one on each call.
    """
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    """
    Create a function that accumulates spell power over time.

    The returned function adds a given amount to an internal power
    total and returns the updated value.

    Args:
        initial_power (int): The starting power level.

    Returns:
        callable: A function that takes an integer amount and
        adds it to the stored total power.
    """
    total_power = initial_power

    def accumulate(amount: int):
        nonlocal total_power
        total_power += amount
        return total_power

    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:
    """
    Create an enchantment function for a specific enchantment type.

    The returned function applies the chosen enchantment to an item
    name and returns the enchanted item description.

    Args:
        enchantment_type (str): The type of enchantment to apply.

    Returns:
        callable: A function that takes an item name and returns
        a string describing the enchanted item.
    """

    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, callable]:
    """
    Create a simple in-memory storage system using closures.

    The vault allows values to be stored and retrieved using
    string keys. It exposes two functions: one for storing
    values and another for recalling them.

    Returns:
        dict[str, callable]: A dictionary containing two functions:
            - 'store': saves a value associated with a key.
            - 'recall': retrieves a value by key, or returns
              'Memory not found' if the key does not exist.
    """
    memory = {}

    def store(key: str, value: any):
        memory[key] = value

    def recall(key: str) -> any:
        return memory.get(key, "Memory not found")

    return {
        'store': store,
        'recall': recall
    }


def main():
    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("\nTesting enchantment factory...")
    flaming_enchantment = enchantment_factory("Flaming")
    frozen_enchantment = enchantment_factory("Frozen")

    print(flaming_enchantment("Sword"))
    print(frozen_enchantment("Shield"))


if __name__ == "__main__":
    main()
