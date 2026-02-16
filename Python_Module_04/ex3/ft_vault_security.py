#!/usr/bin/env python3
"""
Cyber Archives vault security script.

Reads classified data from a secure file and appends
new security records using protected access.
"""


def main():
    """
    Main vault security routine.

    Extracts classified information, appends new
    security entries, and ensures safe file handling.
    """
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    with open("classified_data.txt", "r") as file:
        print("Vault connection established with failsafe protocols")
        print("SECURE EXTRACTION:")
        print(f"{file.read()}")
    with open("classified_data.txt", "a") as file:
        print("SECURE PRESERVATION:")
        print("[CLASSIFIED] New security protocols archived")
        file.write("\n[CLASSIFIED] New security protocols archived")
        print("Vault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
