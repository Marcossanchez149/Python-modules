#!/usr/bin/env python3

'''
    Base class for all garden-related errors.
'''


class GardenError(Exception):
    def __init__(self, message="There is an error"):
        super().__init__(message)


'''
    Raised when there is a problem with a plant.
'''


class PlantError(GardenError):
    def __init__(self, message="The tomato plant is wilting!"):
        super().__init__(message)


'''
    Raised when there is a water-related problem.
'''


class WaterError(GardenError):
    def __init__(self, message="Not enough water in the tank!"):
        super().__init__(message)


'''
    Tests custom garden exceptions.
'''


def test_errors():
    print("=== Custom Garden Errors Demo ===")
    print("Testing PlantError...")
    try:
        raise PlantError()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("Testing WaterError...")
    try:
        raise WaterError()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("Testing catching all garden errors...")
    try:
        raise PlantError()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise WaterError()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_errors()
