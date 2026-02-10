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


class Flower(Plant):
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
        return (f'(Flower) {super().get_info()}, {self.__color}')


'''
Represents a tree, which is a type of plant with a trunk diameter.

This class extends the Plant class by adding a trunk diameter attribute
and functionality to calculate the shade produced by the tree.
'''


class Tree(Plant):
    '''
    Attributes:
        __trunk_diameter(int):
        Diameter of the tree trunk in centimeters (private).
    '''
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        self.__trunk_diameter = trunk_diameter
        super().__init__(name, height, age)

    '''
    produce_shade():
            Calculates and prints the area of shade provided by the tree.
    '''
    def produce_shade(self):
        shade = (((self.__trunk_diameter/2) ** 2) * 3.1415)
        print(f'{self.name} provides {shade} square meters of shade')

    '''
    get_info() -> str:
            Returns a readable string with the tree's information,
            including trunk diameter.
    '''
    def get_info(self):
        return f'(Tree){super().get_info()},{self.__trunk_diameter}cm diameter'


'''
Represents a vegetable, which is a type of plant grown for consumption.

This class extends the Plant class by adding harvest season and
nutritional value attributes, along with logic to describe its nutrition.
'''


class Vegetable(Plant):
    '''
     __harvest_season (str):
        The season in which the vegetable is harvested (private).
    __nutritional_value (int):
        Nutritional value score of the vegetable (private).
    '''
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: int):
        self.__harvest_season = harvest_season
        self.__nutritional_value = nutritional_value
        super().__init__(name, height, age)

    '''
    get_nutritional_value():
            Prints a message describing the vegetable's nutritional richness.
    '''
    def get_nutritional_value(self):
        if (self.__nutritional_value > 50):
            print(f'{self.name} is rich in vitamin C')
        else:
            print(f'{self.name} is rich in vitamin D')

    '''
    get_info() -> str:
            Returns a readable string with the vegetable's information,
            including harvest season.
    '''
    def get_info(self):
        return (f'(Vegetable){super().get_info()},'
                f'{self.__harvest_season} harvest')


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    flower1 = Flower("Rose", 25, 30, "red color")
    tree1 = Tree("Oak", 500, 1825, 50)
    vegetable1 = Vegetable("Tomato", 80, 90, "summer", 90)
    flower2 = Flower("Lilie", 95, 35, "red color")
    tree2 = Tree("Pine", 320, 2825, 90)
    vegetable3 = Vegetable("Pepper", 60, 100, "summer", 30)
    print(flower1.get_info())
    flower1.bloom()
    print(tree1.get_info())
    tree1.produce_shade()
    print(vegetable1.get_info())
    vegetable1.get_nutritional_value()
