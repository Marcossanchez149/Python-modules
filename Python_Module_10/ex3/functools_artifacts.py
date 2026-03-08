import operator
import functools

def spell_reducer(spells: list[int], operation: str) -> int:
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
    return {
        'fire_enchant': functools.partial(base_enchantment, 50, 'fire'),
        'ice_enchant': functools.partial(base_enchantment, 50, 'ice'),
        'lightning_enchant': functools.partial(base_enchantment, 50, 'lightning')
    }
    
@functools.lru_cache(maxsize=None)    
def memoized_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)

    
def spell_dispatcher() -> callable:

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