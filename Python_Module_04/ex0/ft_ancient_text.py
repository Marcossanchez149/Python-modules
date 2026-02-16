#!/usr/bin/env python3
"""
Cyber Archives data recovery script.

Attempts to access a text file and display its contents,
handling basic errors if the file is not found.
"""


def main():
    """
    Main entry point of the program.

    Opens a target file, reads and prints its contents,
    and handles errors during the access process.
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    route = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {route}")
    try:
        file = open(route)
        print("Connection established...")
        print(f"RECOVERED DATA: \n{file.read()}")
        file.close()
        print("Data recovery complete. Storage unit disconnected.")
    except Exception:
        print(" ERROR: Storage vault not found")


if __name__ == "__main__":
    main()
