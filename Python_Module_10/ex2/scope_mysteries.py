def mage_counter() -> callable:
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
        
    return counter


def spell_accumulator(initial_power: int) -> callable:
    total_power = initial_power

    def accumulate(amount: int):
        nonlocal total_power
        total_power += amount
        return total_power
        
    return accumulate
    
def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant

    
def memory_vault() -> dict[str, callable]:
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