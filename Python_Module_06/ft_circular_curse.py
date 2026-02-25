#!/usr/bin/env python3
from alchemy.grimoire import validate_ingredients, record_spell


def main():
    print("=== Circular Curse Breaking ===")
    print("Testing ingredient validation:")
    res1 = validate_ingredients("fire air")
    print(f'validate_ingredients("fire air"): {res1}')
    res2 = validate_ingredients("dragon scales")
    print(f'validate_ingredients("dragon scales"): {res2}')
    print("Testing spell recording with validation:")
    rec1 = record_spell("Fireball", "fire air")
    print(f'record_spell("Fireball", "fire air"): {rec1}')
    rec2 = record_spell("Dark Magic", "shadow")
    print(f'record_spell("Dark Magic", "shadow"): {rec2}')
    print("Testing late import technique:")
    rec3 = record_spell("Lightning", "air")
    print(f'record_spell("Lightning", "air"): {rec3}')
    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
