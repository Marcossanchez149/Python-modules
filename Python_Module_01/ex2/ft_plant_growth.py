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
        print(f'{self.name}: {self.__height}cm, {self.__ageDays} days old')
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
    plant1 = Plant("Rose", 25, 30)
    days = 6
    print("=== Day 1 ===")
    plant1.get_info()
    print(f'=== Day {days} ===')
    plant1.grow(days)
    plant1.age(days)
    plant1.get_info()
    print(f'Growth this week: +{days}cm')
