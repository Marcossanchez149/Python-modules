#!/usr/bin/env python3

'''
    Raised when there is not enough water.
'''


class WaterError(Exception):
    def __init__(self, message="Not enough water in the tank!"):
        super().__init__(message)


'''
    Raised when invalid plant data is detected.
'''


class InvalidError(Exception):
    def __init__(self, message):
        super().__init__(message)


'''
    Represents a plant with water and sunlight requirements.
'''


class Plant:
    def __init__(self, name: str, water_level: int, sunlight_hours: int):
        self.set_name(name)
        self.set_water_level(water_level)
        self.set_sunlight_hours(sunlight_hours)

    '''
        Sets the plant name.
    '''
    def set_name(self, name):
        if (not name.strip()):
            raise (InvalidError(" Plant name cannot be empty!"))
        else:
            self.__name = name

    '''
        Sets and validates water level.
    '''
    def set_water_level(self, water_level):
        if (water_level > 10):
            raise (InvalidError(f'Water level {water_level}'
                                'is too high(max 10)'))
        elif (water_level < 1):
            raise (InvalidError(f'Water level {water_level} '
                                f'is too high(min 1)'))
        else:
            self.__water_level = water_level

    '''
        Sets and validates sunlight hours.
    '''
    def set_sunlight_hours(self, sunlight_hours):
        if (sunlight_hours > 12):
            raise (InvalidError(f'Sunlight hours {sunlight_hours}'
                                f'is too high(max 12)'))
        elif (sunlight_hours < 2):
            raise (InvalidError(f'Sunlight hours {sunlight_hours}'
                                f'is too high(min 2)'))
        else:
            self.__sunlight_hours = sunlight_hours

    '''
        Sets values without validation (unsafe).
    '''
    def set_no_check(self, water_level, sunlight_hours):
        self.__water_level = water_level
        self.__sunlight_hours = sunlight_hours

    '''
        Returns water level
    '''
    def get_water_level(self):
        return (self.__water_level)

    '''
        Returns plants name
    '''
    def get_name(self):
        return (self.__name)

    '''
        Returns sunlight hours
    '''
    def get_sunlight_hours(self):
        return (self.__sunlight_hours)

    '''
        Checks if plant parameters are within safe limits.
    '''
    def check_health(self):
        if (self.__sunlight_hours > 12 or self.__water_level > 10
           or self.__sunlight_hours < 2 or self.__water_level < 1):
            raise (InvalidError("Plant is in danger"))
        else:
            return (f'Heathy (water:{self.__water_level},'
                    f'sun: {self.__sunlight_hours})')


'''
    Manages plants and garden operations.
'''


class GardenManager:

    def __init__(self, name):
        self.__name = name
        self.__plants: list[Plant] = []

    '''
        Adds a new plant to the garden.
    '''
    def add_plant(self, plant_name, water_level, sunlight_hours):
        try:
            plant = Plant(plant_name, water_level, sunlight_hours)
            self.__plants.append(plant)
            print(f'Added {plant_name} successfully')
        except InvalidError as e:
            print(f'Error adding plant: {e}')

    '''
        Waters plants and handles water errors.
    '''
    def water_plant(self):
        print("Opening watering system")
        try:
            for plant in self.__plants:
                if (plant.get_water_level() < 3):
                    raise (WaterError)
                print(f'Watering {plant.get_name()} -success')
        except WaterError as e:
            print(f'Error: {e}')
        finally:
            print("Closing watering system (cleanup)")

    '''
        Checks health status of all plants.
    '''
    def check_plant_health(self):
        print("Checking plants health...")
        try:
            for plant in self.__plants:
                print(f'{plant.get_name()}: {plant.check_health()}')
        except InvalidError as e:
            print(f'Error checking {plant.get_name()}: {e}')

    '''
        Return plants
    '''
    def get_plants(self):
        return (self.__plants)

    '''
        Set plants values
    '''
    def set_plants(self, plants):
        self.__plants = plants


if __name__ == "__main__":
    manager = GardenManager("Test")
    manager.add_plant("", 6, 5)
    manager.add_plant("tomato", 9, 6)
    manager.add_plant("lettuce", 6, 5)
    manager.add_plant("lettuce", 6, 5)
    plants = manager.get_plants()
    plants[2].set_no_check(10, 20)
    manager.set_plants(plants)
    manager.water_plant()
    manager.check_plant_health()
