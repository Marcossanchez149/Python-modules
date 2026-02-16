#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    scores = []
    lenght = len(sys.argv)
    if (lenght == 1):
        print(f'No scores provided. Usage: python3 '
              f'{sys.argv[0]} <score1> <score2> ...')
    else:
        cont = 1
        try:
            while (cont < lenght):
                scores.append(int(sys.argv[cont]))
                cont += 1
            print(f'Scores processed: {scores}')
            print(f'Total players: {len(scores)}')
            print(f'Total score: {sum(scores)}')
            print(f'Average score: {(sum(scores)/len(scores)):.2f}')
            print(f'High score: {max(scores)}')
            print(f'Low score: {min(scores)}')
            print(f'Score range: {(max(scores) - min(scores))}')
        except ValueError:
            print("There is a wrong value")
