#!/usr/bin/env python3
"""
Cyber Archives preservation script.

Creates a new archive file, writes preservation data into it,
and displays the stored contents.
"""


def main():
    """
    Main execution function.

    Creates a text file, writes predefined archive entries,
    reads the file back, and handles basic runtime errors.
    """
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    try:
        print("Initializing new storage unit: new_discovery.txt")
        file = open("new_discovery.txt", "w")
        print("Storage unit created successfully...")
        print("Inscribing preservation data...")
        file.write("[ENTRY 001] New quantum algorithm discovered \n"
                   "[ENTRY 002] Efficiency increased by 347% \n"
                   "[ENTRY 003] Archived by Data Archivist trainee \n")
        file.close()
        file = open("new_discovery.txt")
        print(f"{file.read()}")
        print("Data inscription complete. Storage unit sealed.")
        file.close()
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except Exception:
        print("There has been some error")
        file.close()


if __name__ == "__main__":
    main()
