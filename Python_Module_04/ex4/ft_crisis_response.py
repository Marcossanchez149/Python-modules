#!/usr/bin/env python3
"""
Cyber Archives crisis response script.

Attempts to access multiple archive files while handling
common access-related errors.
"""


def access_file(file_name):
    """
    Attempts to open and read a given file.

    Handles missing files and permission errors
    during archive access.
    """
    try:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        with open(file_name) as file:
            print(file.read())
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")


def main():
    """
    Main crisis response workflow.

    Executes a sequence of archive access attempts
    and reports system status after each operation.
    """
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    access_file("lost_archive.txt")
    print("STATUS: Crisis handled, system stable")
    access_file("security_protocols.txt")
    print("STATUS: Crisis handled, security maintained")
    access_file("standard_archive.txt")
    print("STATUS: Normal operations resumed")


if __name__ == "__main__":
    main()
