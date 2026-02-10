#!/usr/bin/env python3

'''
    Validates plant health parameters.
    Raises ValueError if any value is invalid.
'''


def check_plant_health(plant_name, water_level, sunlight_hours):
    if (not plant_name.strip()):
        raise (ValueError(" Plant name cannot be empty!"))
    if (water_level > 10):
        raise (ValueError(f'Water level {water_level} is too high (max 10)'))
    if (water_level < 1):
        raise (ValueError(f'Water level {water_level} is too high (min 1)'))
    if (sunlight_hours > 12):
        raise (ValueError(f'Water level {sunlight_hours} is too high(max 12)'))
    if (sunlight_hours < 2):
        raise (ValueError(f'Water level {sunlight_hours} is too high (min 2)'))
    return (f'Plant {plant_name} is healthy!')


'''
    Tests plant health validation with valid and invalid inputs.
'''


def test_plant_checks():
    print("=== Garden Plant Health Checker ===")
    print("Testing good values...")
    print(check_plant_health("tomato", 5, 8))
    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 5)
    except ValueError as e:
        print(f'Error: {e}')
    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 20, 5)
    except ValueError as e:
        print(f'Error: {e}')
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(f'Error: {e}')


if __name__ == "__main__":
    test_plant_checks()
