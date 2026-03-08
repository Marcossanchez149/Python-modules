def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined_spell(target):
        return (spell1(target), spell2(target))
    return combined_spell


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified_spell():
        return base_spell() * multiplier
        
    return amplified_spell
    
def conditional_caster(condition: callable, spell: callable) -> callable:
    def cast_if_true(target):
        if condition(target):
            return spell(target)
        return "Spell fizzled"
        
    return cast_if_true

    
def spell_sequence(spells: list[callable]) -> callable:
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