#!/usr/bin/env python3

from enum import Enum
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, model_validator, ValidationError


class Rank(str, Enum):
    """
    Enumeration of possible crew ranks.

    Values:
        cadet: Entry-level trainee crew member.
        officer: Standard operational crew member.
        lieutenant: Mid-level officer with operational responsibility.
        captain: Senior leader responsible for mission operations.
        commander: Highest authority responsible for overall mission command.
    """
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    """
    Data model representing a crew member assigned to a mission.

    Attributes:
        member_id (str): Unique identifier for the crew member.
            Must be between 3 and 10 characters.
        name (str): Full name of the crew member.
            Must be between 2 and 50 characters.
        rank (Rank): Rank within the mission hierarchy.
        age (int): Age of the crew member. Must be between 18 and 80.
        specialization (str): Area of expertise or mission role.
            Must be between 3 and 30 characters.
        years_experience (int): Years of professional experience.
            Must be between 0 and 50.
        is_active (bool): Indicates whether the crew
        member is currently active.
    """
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """
    Data model representing a space mission.

    This model contains information about the mission itself and the crew
    assigned to it. It also implements additional validation rules to ensure
    that mission requirements are met.

    Attributes:
        mission_id (str): Unique identifier for the mission.
            Must start with "M".
        mission_name (str): Descriptive name of the mission.
        destination (str): Target destination for the mission.
        launch_date (datetime): Planned launch date and time.
        duration_days (int): Mission duration in days (1–3650).
        crew (List[CrewMember]): List of crew members assigned to the mission.
            Must contain between 1 and 12 members.
        mission_status (str): Current status of the mission
            (default is "planned").
        budget_millions (float): Mission budget in millions of dollars
            (1.0–10000.0).
    """
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_rules(self):
        """
        Apply additional mission-level validation rules.

        Rules enforced:
        - Mission ID must start with "M".
        - The crew must include at least one Captain or Commander.
        - Long missions (> 365 days) require at least 50% experienced
          crew members (5+ years of experience).
        - All crew members must be active.

        Returns:
            SpaceMission: The validated mission instance.

        Raises:
            ValueError: If any mission requirement is violated.
        """
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        has_leadership = any(
            member.rank in [Rank.commander, Rank.captain]
            for member in self.crew
        )
        if not has_leadership:
            raise ValueError('Mission must have at least'
                             ' one Commander or Captain')

        if self.duration_days > 365:
            veterans = sum(1 for m in self.crew if m.years_experience >= 5)
            if veterans < (len(self.crew) / 2):
                raise ValueError('Long missions (> 365 days) need '
                                 '50% experienced crew (5+ years)')

        if any(not member.is_active for member in self.crew):
            raise ValueError('All crew members must be active')

        return self


def main():
    """
    Main entry point of the script.

    Demonstrates the validation of crew members and space missions by:
    1. Creating a valid mission with a proper leadership structure.
    2. Attempting to create an invalid mission to trigger validation errors.
    """
    print("Space Mission Crew Validation")
    print("============================================")

    try:
        cmdr = CrewMember(
            member_id="C001", name="Sarah Connor", rank="commander",
            age=35, specialization="Mission Command", years_experience=10
        )
        lt = CrewMember(
            member_id="L002", name="John Smith", rank="lieutenant",
            age=29, specialization="Navigation", years_experience=6
        )
        off = CrewMember(
            member_id="O003", name="Alice Johnson", rank="officer",
            age=25, specialization="Engineering", years_experience=2
        )

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2024-05-20",
            duration_days=900,
            crew=[cmdr, lt, off],
            budget_millions=2500.0
        )

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(f"- {member.name} ({member.rank.value}) -"
                  f"{member.specialization}")

    except ValidationError as e:
        print(e)

    print("============================================")

    print("Expected validation error:")
    try:
        cadet1 = CrewMember(
            member_id="K001", name="Rookie One", rank="cadet",
            age=19, specialization="Cleaning", years_experience=0
        )

        bad_mission = SpaceMission(
            mission_id="M2025_FAIL",
            mission_name="Doomed Mission",
            destination="Moon",
            launch_date="2025-01-01",
            duration_days=10,
            crew=[cadet1],
            budget_millions=10.0
        )
        print(bad_mission)
    except ValidationError as e:
        for error in e.errors():
            msg = error['msg'].replace('Value error, ', '')
            print(f"{msg}")


if __name__ == "__main__":
    main()
