#!/usr/bin/env python3
import sys
import os
import site


def main():
    """
    Entry point of the script.

    The function determines whether the current Python interpreter
    is running inside a virtual environment by comparing:
        sys.prefix and sys.base_prefix

    Behavior:
    - If both values are equal, Python is running in the global
      environment (no virtual environment active).
    - If they differ, Python is running inside a virtual environment.

    The function then prints informative messages about the environment,
    including the interpreter path and the package installation location.
    """
    if (sys.prefix == sys.base_prefix):
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("WARNING: You're in the global environment!"
              "\nThe machines can see everything you install.")
        print("To enter the construct, run:"
              "\npython -m venv matrix_env"
              "\nsource matrix_env/bin/activate # On Unix"
              "\nmatrix_env"
              "\nScripts"
              "\nactivate # On Windows"
              "\n·Then run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        env_path = sys.prefix
        env_name = os.path.basename(env_path)
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env_path}")
        print("SUCCESS: You're in an isolated environment!"
              "\nSafe to install packages without affecting"
              "\nthe global system.")
        print("\nPackage installation path:")
        site_packages = site.getsitepackages()[0]
        print(site_packages)


if __name__ == "__main__":
    main()
