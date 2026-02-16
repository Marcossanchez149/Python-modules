#!/usr/bin/env python3

import sys
import math


def calcule_distance(x1, x2, y1, y2, z1, z2):
    return (math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))


def check_distance(position):
    try:
        for pos in position:
            pos = int(pos)
        position_tuple = tuple(position)
        print(f'Position created:{position_tuple}')
        distance = calcule_distance(0, 0, 0, position_tuple[0],
                                    position_tuple[1], position_tuple[2])
        print(f'Distance between (0, 0, 0) and {position_tuple}:'
              f' {float(distance):.2f}')
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details: - Type: ValueError, Args: {e}")


if __name__ == "__main__":
    print(f"{sys.argv[0]}")
    print("=== Game Coordinate System ===")
    position = (10, 20, 5)
    check_distance(position)
    position = (3, 4, 0)
    check_distance(position)
    position = ("abc", "def", "ghi")
    check_distance(position)
    print("Unpacking demonstration:")
    position = (3, 4, 0)
    position_tuple = tuple(position)
    print(f"Player at x={3}, y={4}, z={0}")
    print(f"Coordinates: X={3}, Y={4}, Z={0}")
