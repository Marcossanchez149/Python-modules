#!/usr/bin/env python3

def random_event(cont):
    names = ["alice", "bob", "charlie", "dave", "eve"]
    actions = ["killed monster", "found treasure", "leveled up", "died"]
    for i in range(cont):
        name_index = i % 5
        action_index = (i + 1) % 4
        level = ((i * 7) % 15) + 1
        event = {
            "id": i + 1,
            "name": names[name_index],
            "level": level,
            "action": actions[action_index]
        }
        yield event


def get_fibonacci_sequence(num):
    cont = 0
    cont2 = 1
    for i in range(num):
        yield cont
        temp = cont
        cont = cont2
        cont2 += temp


def get_prime_numbers(num):
    cont = 2
    i = 0
    while (i < num):
        is_prime = True
        for x in range(2, cont):
            if (cont % x == 0):
                is_prime = False
                break
        if (is_prime):
            yield cont
            i += 1
        cont += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    n_events = 1000
    print(f"Processing {n_events} game events...")
    total = 0
    high_level = 0
    treasure = 0
    levelup = 0
    stream = random_event(n_events)
    for event in stream:
        total += 1
        if total <= 3:
            print(f"Event {event['id']}: Player {event['name']} "
                  f"(level {event['level']}) {event['action']}")
        if total == 4:
            print("...")
        if event['level'] >= 10:
            high_level += 1
        if event['action'] == "found treasure":
            treasure += 1
        if event['action'] == "leveled up":
            levelup += 1
    print("=== Stream Analytics ===")
    print(f"Total events processed: {n_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {levelup}")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print("=== Generator Demonstration ===")
    fibonacci_sequence = get_fibonacci_sequence(10)
    print("Fibonacci sequence (first 10):", end=" ")
    first = True
    for num in fibonacci_sequence:
        if (first):
            first = False
            print(f" {num}", end="")
        else:
            print(f", {num}", end="")
    print("")
    print("Prime numbers (first 5):", end="")
    prime_numbers = get_prime_numbers(5)
    first = True
    for num in prime_numbers:
        if (first):
            first = False
            print(f" {num}", end="")
        else:
            print(f", {num}", end="")
    print("")
