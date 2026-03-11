#!/usr/bin/env python3

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """
    Data model representing a space station.

    This model uses Pydantic to enforce validation rules for each field.
    The constraints ensure that the station data remains within realistic
    operational limits.

    Attributes:
        station_id (str): Unique identifier for the station.
            Must be between 3 and 10 characters.
        name (str): Human-readable name of the space station.
            Must be between 1 and 50 characters.
        crew_size (int): Number of crew members currently aboard.
            Must be between 1 and 20.
        power_level (float): Current power level percentage.
            Must be between 0.0 and 100.0.
        oxygen_level (float): Current oxygen level percentage.
            Must be between 0.0 and 100.0.
        last_maintenance (datetime): Timestamp of the last
        maintenance operation.
        is_operational (bool): Indicates whether the station
        is currently operational.
            Defaults to True.
        notes (Optional[str]): Optional notes about the station.
            Maximum length of 200 characters.
    """
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main():
    """
    Main entry point of the script.

    This function demonstrates how the SpaceStation model validates input data.
    It performs two tests:

    1. Creates a valid space station instance and prints its information.
    2. Attempts to create an invalid space station instance to trigger
       validation errors and prints the corresponding error messages.
    """
    print("Space Station Data Validation")
    print("==================================")
    try:
        valid_station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2023-11-15T14:30:00",
            is_operational=True
        )

        print("Valid station created:")
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        if valid_station.is_operational:
            status = "Operational"
        else:
            status = "Offline"
        print(f"Status: {status}")

    except ValidationError as e:
        print(f"Unexpected error: {e}")

    print("================================")

    print("Expected validation error:")
    try:
        invalid_station = SpaceStation(
            station_id="DS9",
            name="Deep Space Nine",
            crew_size=500,
            power_level=100.0,
            oxygen_level=100.0,
            last_maintenance=datetime.now()
        )
        print(invalid_station)
    except ValidationError as e:
        for error in e.errors():
            print(f"Error in {error['loc'][0]}: {error['msg']}")


if __name__ == "__main__":
    main()
