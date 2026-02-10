#!/usr/bin/env python3
'''
A class that represents a secure plant.
It stores basic information such as the plant's name, height,
and age, and can print this information in a readable way.
'''


class SecurePlant:
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
            print(f'Height updated: {height}cm [OK]')
        else:
            print("Security: Negative height rejected")

    '''
    set_age(age: int): Sets the plant's age if the value is positive.
    '''
    def set_age(self, age: int):
        if (age > 0):
            self.__age = age
            print(f'Height updated: {age}days [OK]')
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
        return (f'{self.name} ({self.__height}cm, {self.__age} days)')


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)
    plant.set_height(-9)
    print(plant.get_info())
