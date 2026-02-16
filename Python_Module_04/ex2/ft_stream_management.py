#!/usr/bin/env python3
import sys

"""
Cyber Archives communication script.

Collects user input to simulate an archive status report and
sends standard and diagnostic messages to different output streams.
"""


def main():
    """
    Main communication handler.

    Reads archivist input, prints a formatted status message,
    and outputs a diagnostic alert to the error stream.
    """
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    id = input("Input Stream active. Enter archivist ID:")
    status = input("Input Stream active. Enter status report:")
    sys.stdout.write(f"[STANDARD] Archive status from {id}: {status} \n")
    sys.stderr.write("[ALERT] System diagnostic: "
                     "Communication channels verified \n")
    sys.stdout.write("[STANDARD] Data transmission complete \n")
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
