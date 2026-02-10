#!/usr/bin/env python3

'''
    Raised when an invalid plant is found.
'''


class PlantError(Exception):
    def __init__(self, message="Cannot water None - invalid plant!"):
        super().__init__(message)


'''
    Waters all plants in the list and
    ensures cleanup with finally.
'''


def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if (not plant.strip()):
                raise (PlantError)
            print(f'Watering {plant}')
    except PlantError as e:
        print(f'Error: {e}')
    finally:
        print("Closing watering system (cleanup)")


'''
    Tests watering with an invalid plant entry.
'''


def test_watering_system():
    plant_list = [("tomato"), (""), ("carrots")]
    print("Opening watering system")
    try:
        for plant in plant_list:
            if (not plant.strip()):
                raise (PlantError)
            else:
                print(f'Watering {plant}')
    except PlantError as e:
        print(f'Error: {e}')
    finally:
        print("Closing watering system (cleanup)")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    plant_list = [("tomato"), ("lettuce"), ("carrots")]
    print("Testing normal watering...")
    water_plants(plant_list)
    print("Testing with error...")
    test_watering_system()
