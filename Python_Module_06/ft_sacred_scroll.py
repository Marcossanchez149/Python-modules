#!/usr/bin/env python3
import alchemy


def main():
    print("=== Sacred Scroll Mastery ===")
    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire():{alchemy.elements.create_fire()} \n"
          f"alchemy.elements.create_water():{alchemy.elements.create_water()}"
          f"\n"
          f"alchemy.elements.create_earth():{alchemy.elements.create_earth()}"
          f"\n"
          f"alchemy.elements.create_air():{alchemy.elements.create_air()}")
    print("Testing package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")
    try:
        print(f"alchemy.create_earth(): {alchemy.create_earth()}")
    except Exception:
        print("alchemy.create_earth(): AttributeError - not exposed")
    try:
        print(f"alchemy.create_air(): {alchemy.create_air()}")
    except Exception:
        print("alchemy.create_air(): AttributeError - not exposed")
    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
