
def healing_potion() -> str:
    from .elements import create_fire as fire, create_water as water
    return (f"Healing potion brewed with "
            f"{fire()} and {water()}")


def strength_potion() -> str:
    from alchemy.elements import create_earth, create_fire
    return (f"Strength potion brewed with "
            f"{create_earth()} and {create_fire()}")


def invisibility_potion() -> str:
    from .elements import create_air, create_water
    return (f"Invisibility potion brewed with "
            f"{create_air()} and {create_water()}")


def wisdom_potion() -> str:
    import alchemy.elements
    return (f"Wisdom potion brewed with all elements: "
            f"{alchemy.elements.create_fire()},"
            f"{alchemy.elements.create_water()}"
            f"{alchemy.elements.create_air()},"
            f"{alchemy.elements.create_earth()}")
