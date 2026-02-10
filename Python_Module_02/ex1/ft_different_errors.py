#!/usr/bin/env python3


'''
    Demonstrates how different Python errors
    can be raised and handled using try/except.
'''


def garden_operations():
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print("Testing ZeroDivisionError...")
    try:
        divide_by_zero = (42/0)
        print(divide_by_zero)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    print("Testing FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    print("Testing KeyError...")
    try:
        dictionary = {"Name": "Alice", "plants": 6}
        print(dictionary["missing_plant"])
    except KeyError as e:
        print(f"Caught KeyError: {e}")


'''
    Runs all error tests and checks that
    the program continues after exceptions.
'''


def test_error_types():
    garden_operations()
    print("Testing multiple errors together...")
    try:
        int("world")
        divide_by_zero = (42/0)
        print(divide_by_zero)
        open("missing.txt")
        dictionary = {"Name": "Alice", "plants": 6}
        print(dictionary["plant"])
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Found an error")
    finally:
        print("Program continues!")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
