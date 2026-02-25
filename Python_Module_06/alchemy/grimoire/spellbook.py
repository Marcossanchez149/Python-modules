
def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    awnser = validate_ingredients(ingredients)
    if (awnser.endswith("- VALID")):
        return (f"Spell recorded: {spell_name} ({awnser})")
    else:
        return (f"Spell rejected: {spell_name} ({awnser})")
