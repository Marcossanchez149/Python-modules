

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
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
        print(f"{first['name']} ({first['power']} power) comes before {second['name']} ({second['power']} power)")
    print("\nTesting spell transformer...")
    transformed_spells = spell_transformer(spells)
    print(" ".join(transformed_spells))


if __name__ == "__main__":
    main()
