#!/usr/bin/env python3

import sys


if __name__ == "__main__":
    print("=== Command Quest ===")
    len = len(sys.argv)
    print(f'Program name: {sys.argv[0]}')
    if (len == 1):
        print("No arguments provided!")
    else:
        print(f'Arguments received: {len - 1}')
        cont = 1
        while (cont < len):
            print(f'Argument {cont}: {sys.argv[cont]}')
            cont += 1
    print(f'Total arguments: {len}')
