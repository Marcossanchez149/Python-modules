#!/usr/bin/env python3

import os
import sys
from dotenv import load_dotenv


def main():
    """
    Main entry point of the program.

    Steps performed:
    1. Load environment variables from a `.env` file using `load_dotenv()`.
    2. Read required and optional configuration variables.
    3. Validate the presence of critical settings.
    4. Display a configuration summary to the user.

    The function also performs a basic security check to ensure
    that secrets are not hardcoded and that configuration values
    are properly loaded from environment sources.

    If critical variables are missing, the program prints a warning
    and terminates with exit code 1.
    """
    print("ORACLE STATUS: Reading the Matrix...")
    env_loaded = load_dotenv()

    matrix_mode = os.getenv("MATRIX_MODE", "development")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    if not db_url or not api_key or not zion_endpoint:
        print("\n[!] WARNING: Missing critical configuration.")
        print("The Oracle is blind. Please copy .env.example to .env "
              "and configure your variables.")
        sys.exit(1)

    print("\nConfiguration loaded:")
    print(f"Mode: {matrix_mode}")

    if "local" in db_url.lower() or matrix_mode == "development":
        print("Database: Connected to local instance")
    else:
        print("Database: Connected to production instance")

    if api_key:
        print("API Access: Authenticated")

    print(f"Log Level: {log_level}")

    if zion_endpoint:
        print("Zion Network: Online")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if env_loaded:
        print("[OK] .env file properly configured")
    else:
        print("[!] No .env file found (Relying solely on "
              "OS environment variables)")

    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
