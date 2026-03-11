#!/usr/bin/env python3

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """
    Sort a list of magical artifacts by their power level in descending order.

    Args:
        artifacts (list[dict]): A list of dictionaries where each dictionary
            represents an artifact and must contain a 'power' key.

    Returns:
        list[dict]: A new list of artifacts sorted from highest
        to lowest power.
    """
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """
    Filter a list of mages based on a minimum power threshold.

    Args:
        mages (list[dict]): A list of dictionaries representing mages.
            Each mage dictionary must contain a 'power' key.
        min_power (int): The minimum power level required for a mage
            to be included in the result.

    Returns:
        list[dict]: A list of mages whose power is greater than or equal
        to the specified minimum power.
    """
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """
    Transform a list of spell names by decorating each spell with
    asterisks for stylistic formatting.

    Args:
        spells (list[str]): A list of spell names as strings.

    Returns:
        list[str]: A list of transformed spell strings formatted
        as "* spell *".
    """
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """
    Calculate basic statistics about the power levels of a group of mages.

    The function computes the maximum power, minimum power, and
    average power among the given mages.

    Args:
        mages (list[dict]): A list of dictionaries representing mages.
            Each dictionary must contain a 'power' key.

    Returns:
        dict: A dictionary containing:
            - 'max_power' (int): The highest power value.
            - 'min_power' (int): The lowest power value.
            - 'avg_power' (float): The average power rounded to two decimals.

        If the list of mages is empty, all values will be zero.
    """
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    max_p = max(mages, key=lambda x: x['power'])['power']
    min_p = min(mages, key=lambda x: x['power'])['power']
    total_power = sum(map(lambda x: x['power'], mages))
    avg_p = round(total_power / len(mages), 2)

    return {
        'max_power': max_p,
        'min_power': min_p,
        'avg_power': avg_p
    }


def main():
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'magic'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'}
    ]
    spells = ['fireball', 'heal', 'shield']
    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    if len(sorted_artifacts) >= 2:
        first = sorted_artifacts[0]
        second = sorted_artifacts[1]
        print(f"{first['name']} ({first['power']} power) comes "
              f"before {second['name']} ({second['power']} power)")
    print("\nTesting spell transformer...")
    transformed_spells = spell_transformer(spells)
    print(" ".join(transformed_spells))


if __name__ == "__main__":
    main()
