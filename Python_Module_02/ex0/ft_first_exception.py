#!/usr/bin/env python3
'''
    Converts a string to an integer and checks
    if the temperature is suitable for plants.
'''


def check_temperature(temp_str):
    try:
        temp = int(temp_str)
        if (temp > 0 & temp < 40):
            print(f'Temperature {temp}°C is perfect for plants!')
            return (temp)
        elif (temp > 40):
            print(f'Error: {temp}°C is too hot for plants (max 40°C)')
        else:
            print(f'Error: {temp}°C is too cold for plants (min 0°C)')
    except ValueError:
        print(f'Error: {temp_str} is not a valid number')


'''
    Tests the function with different inputs
    to ensure it handles errors correctly.
'''


def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    temp = "25"
    print(f'Testing temperature: {temp}')
    check_temperature(temp)
    temp = "abc"
    print(f'Testing temperature: {temp}')
    check_temperature(temp)
    temp = "100"
    print(f'Testing temperature: {temp}')
    check_temperature(temp)
    temp = "-50"
    print(f'Testing temperature: {temp}')
    check_temperature(temp)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
