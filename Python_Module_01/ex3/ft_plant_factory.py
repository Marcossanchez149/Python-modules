#!/usr/bin/env python3
'''
A simple class that represents a plant.
It stores basic information such as the plant's name, height,
and age, and can print this information in a readable way.
'''


class Plant:
    '''
    Create a new Plant instance. Its parameters are
    name : str -> The plant's name.
    height : int -> Height of the plant in centimeters.
    age : int -> Age of the plant in days.
    '''
    def __init__(self, name: str, height: int, ageDays: int):
        self.name = name
        self.__height = height
        self.__ageDays = ageDays
    '''
    Return the plant's details.
    '''
    def get_info(self):
        return (f'{self.name} ({self.__height}cm, {self.__ageDays} days)')
    '''
    The plants grow a centimeter per day it receives
    '''
    def grow(self, days):
        self.__height += days
    '''
    The plant adds days to its age per day it receives
    '''
    def age(self, ageDays):
        self.__ageDays += ageDays


if __name__ == "__main__":
    list_plants = []
    plants = [("Rose", 25, 30), ("Oak", 200, 365), ("Cactus", 5, 90),
              ("Sunflower", 80, 45), ("Fern", 15, 120)]
    cont = 0
    for plant_not_created in plants:
        plant = Plant(*plant_not_created)
        print(f'Created: {plant.get_info()}')
        list_plants.append(plant)
        cont += 1
    print(f'Total plants created: {cont}')
