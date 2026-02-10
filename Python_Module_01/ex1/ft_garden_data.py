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
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
    '''
    Print the plant's details.
    '''
    def print_plant(self):
        print(f'{self.name}: {self.height}cm, {self.age} days old')


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    plant1.print_plant()
    plant2.print_plant()
    plant3.print_plant()
