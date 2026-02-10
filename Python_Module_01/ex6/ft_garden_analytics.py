#!/usr/bin/env python3
'''
A class that represents a plant.
It stores basic information such as the plant's name, height,
and age, and can print this information in a readable way.
'''


class Plant:
    '''
    Attributes:
        name (str): The name of the plant.
        __height (int): The plant's height in centimeters (private).
        __age (int): The plant's age in days (private).
    '''
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)

    '''
    set_height(height: int): Sets the plant's height if the value is positive.
    '''
    def set_height(self, height: int):
        if (height > 0):
            self.__height = height
        else:
            print("Security: Negative height rejected")

    '''
    set_age(age: int): Sets the plant's age if the value is positive.
    '''
    def set_age(self, age: int):
        if (age > 0):
            self.__age = age
        else:
            print("Security: Negative age rejected")

    '''
    get_height() -> int: Returns the current height of the plant.
    '''
    def get_height(self):
        return self.__height

    '''
    get_age() -> int: Returns the current age of the plant.
    '''
    def get_age(self):
        return self.__age

    '''
     get_info() -> str: Returns a readable string with the plant's information.
    '''
    def get_info(self):
        return (f'{self.name}: {self.__height}cm, {self.__age} days')


'''
    Represents a flower, which is a type of plant with a specific color.

    This class extends the Plant class by adding a color attribute and
    behavior specific to flowers, such as blooming
'''


class FloweringPlant(Plant):
    '''
    Attributes: __color (str): The color of the flower (private).
    '''
    def __init__(self, name: str, height: int, age: int, color: str):
        self.__color = color
        super().__init__(name, height, age)

    '''
    bloom(): Prints a message indicating that the flower is blooming.
    '''
    def bloom(self):
        print(f'{self.name} is blooming beautifully!')

    '''
    get_info() -> str:
            Returns a readable string with the flower's information,
            including its color.
    '''
    def get_info(self):
        return (f'(Flower) {super().get_info()}, {self.__color} (blooming)')


'''
Represents a prize-winning flower.

This class extends FloweringPlant by adding a point value
used for garden scoring.
'''


class PrizeFlower(FloweringPlant):
    '''
    Attributes: __points (int): The value points of the flower (private).
    '''
    def __init__(self, name: str, height: int, age: int,
                 color: str, points: int):
        self.__points = points
        super().__init__(name, height, age, color)

    '''
    get_info() -> str:
        Returns a readable string with prize flower information,
        including its point value.
    '''
    def get_info(self):
        return (f'(Prize) {super().get_info()},Prize points: {self.__points}')

    '''
    get_points() -> int:
        Returns the prize points of the flower.
    '''
    def get_points(self):
        return (self.__points)


'''
Represents a garden that contains multiple plants.

Gardens can grow plants, calculate prize points,
and generate reports.
'''


class Garden:
    def __init__(self, name: str):
        self.name = name
        self.__plants: list[Plant] = []

    '''
    add_plant(plant: Plant):
        Adds a plant to the garden.
    '''
    def add_plant(self, plant: Plant):
        self.__plants.append(plant)
        print(f'Added {plant.name} to {self.name}`s garden')

    '''
    get_plants() -> list[Plant]:
        Returns the list of plants in the garden.
    '''
    def get_plants(self):
        return self.__plants

    '''
    get_name() -> str:
        Returns the name of the garden.
    '''
    def get_name(self):
        return (self.name)

    '''
    get_points() -> int:
        Calculates and returns the total prize points
        of all prize flowers in the garden.
    '''
    def get_points(self):
        points = 0
        for plant in self.__plants:
            if isinstance(plant, PrizeFlower):
                points += plant.get_points()
        return (points)

    '''
    get_report():
        Prints a detailed report of all plants in the garden.
    '''
    def get_report(self):
        print(f'=== {self.name}`s Garden Report ===')
        print("Plants in garden:")
        for plant in self.__plants:
            print(f' - {plant.get_info()}')

    '''
    grow(day: int):
        Increases the height of all plants by a given number of days.
    '''
    def grow(self, day):
        for plant in self.__plants:
            new_height = plant.get_height() + day
            plant.set_height(new_height)
            print(f'{plant.name} grew {day}cm')


'''
Manages multiple gardens and provides global statistics.
'''


class GardenManager:

    '''
    Internal class used to calculate statistics
    for all managed gardens.
    '''
    class GardenStats:
        def __init__(self, gardens):
            self.__gardens: list[Garden] = gardens

        '''
        get_height_validation():
            Checks that all plants have valid heights.
        '''
        def get_height_validation(self):
            has_valid_height = True
            for garden in self.__gardens:
                for plant in garden.get_plants():
                    if (plant.get_height() < 0):
                        has_valid_height = False
            print(f'Height validation test: {has_valid_height}')

        '''
        get_garden_scores():
            Prints the total prize score of each garden.
        '''
        def get_garden_scores(self):
            print("Garden scores :")
            for garden in self.__gardens:
                print(f'{garden.get_name()}: {garden.get_points()}')

        '''
        get_total_gardens():
            Prints the total number of gardens managed.
        '''
        def get_total_gardens(self):
            cont = 0
            for garden in self.__gardens:
                cont += 1
            print(f'Total gardens managed: {cont}')

    def __init__(self):
        self.__gardens: list[Garden] = []
        self.__garden_stats = self.GardenStats(self.__gardens)

    '''
    add_garden(garden: Garden):
        Adds a garden to the manager.
    '''
    def add_garden(self, garden: Garden):
        self.__gardens.append(garden)

    '''
    get_individual_reports():
        Prints individual reports for each garden.
    '''
    def get_individual_reports(self):
        for garden in self.__gardens:
            garden.get_report()

    '''
    get_complete_reports():
        Prints global statistics for all gardens.
    '''
    def get_complete_reports(self):
        self.__garden_stats.get_height_validation()
        self.__garden_stats.get_garden_scores()
        self.__garden_stats.get_total_gardens()

    '''
    passing_days(day: int):
        Simulates the passing of days for all gardens.
    '''
    def passing_days(self, day):
        for garden in self.__gardens:
            garden.grow(day)

    '''
    create_garden_network() -> GardenManager:
        Creates a demo garden network with sample data.
    '''
    @classmethod
    def create_garden_network(cls):
        print("=== Garden Management System Demo ===")
        plant1 = Plant("Oak Tree", 20, 3)
        plant2 = FloweringPlant("Rose", 6, 2, "red")
        plant3 = PrizeFlower("Sunflower", 12, 1, "yellow", 10)
        plant4 = PrizeFlower("Lile", 14, 6, "Purple", 36)
        manager = GardenManager()
        garden1 = Garden("Alice")
        garden2 = Garden("Bob")
        garden1.add_plant(plant1)
        garden1.add_plant(plant2)
        garden1.add_plant(plant3)
        garden2.add_plant(plant4)
        manager.add_garden(garden1)
        manager.add_garden(garden2)
        return (manager)

    @staticmethod
    def cm_to_meters(cm: int):
        return (cm/100)


if __name__ == "__main__":
    manager = GardenManager.create_garden_network()
    print("\n--- Individual Reports ---")
    manager.get_individual_reports()
    print("\n--- Complete Reports ---")
    manager.get_complete_reports()
    manager.passing_days(15)
    print(f'{manager.cm_to_meters(50)}m')
