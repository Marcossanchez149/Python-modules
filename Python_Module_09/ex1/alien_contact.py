#!/usr/bin/env python3

from enum import Enum
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, model_validator, ValidationError


class ContactType(str, Enum):
    """
    Enumeration of possible alien contact types.

    Values:
        radio: Communication via radio signals.
        visual: Visual sighting without direct interaction.
        physical: Direct physical encounter.
        telepathic: Communication via telepathic means.
    """
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    """
    Data model representing a recorded alien contact event.

    The model validates the structure and constraints of a contact report,
    including identifier formatting, signal limits, and logical rules
    between different fields.

    Attributes:
        contact_id (str): Unique identifier for the contact event.
            Must be between 5 and 15 characters and start with "AC".
        timestamp (datetime): Date and time when the contact occurred.
        location (str): Location where the contact was observed.
            Must be between 3 and 100 characters.
        contact_type (ContactType): Type of alien contact.
        signal_strength (float): Strength of the detected signal
            on a scale from 0.0 to 10.0.
        duration_minutes (int): Duration of the contact event in minutes.
            Must be between 1 and 1440 minutes (24 hours).
        witness_count (int): Number of witnesses present during the event.
            Must be between 1 and 100.
        message_received (Optional[str]): Message received during the
            contact, if any. Maximum length of 500 characters.
        is_verified (bool): Indicates whether the contact report has been
            verified by authorities.
    """
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_rules(self):
        """
        Apply additional cross-field validation rules.

        Rules enforced:
        - The contact ID must start with "AC".
        - Physical contact reports must be verified.
        - Telepathic contact requires at least three witnesses.
        - Strong signals (>7.0) should include a received message.

        Returns:
            AlienContact: The validated model instance.

        Raises:
            ValueError: If any custom validation rule is violated.
        """
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')

        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError('Physical contact reports must be verified')

        if self.contact_type == (ContactType.telepathic and
                                 self.witness_count < 3):
            raise ValueError('Telepathic contact requires '
                             'at least 3 witnesses')

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError('Strong signals (> 7.0) should include '
                             'received messages')

        return self


def main():
    """
    Main entry point of the program.

    Demonstrates the validation behavior of the AlienContact model by:
    1. Creating a valid alien contact report and displaying its data.
    2. Attempting to create an invalid report to trigger validation errors.
    """
    print("Alien Contact Log Validation")
    print("===================================")

    try:
        valid_contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2024-03-20T23:45:00",
            location="Area 51, Nevada",
            contact_type="radio",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )
        print("Valid contact report:")
        print(f"ID: {valid_contact.contact_id}")
        print(f"Type: {valid_contact.contact_type.value}")
        print(f"Location: {valid_contact.location}")
        print(f"Signal: {valid_contact.signal_strength}/10")
        print(f"Duration: {valid_contact.duration_minutes} minutes")
        print(f"Witnesses: {valid_contact.witness_count}")
        print(f"Message: '{valid_contact.message_received}'")
    except ValidationError as e:
        print(e)

    print("===================")

    print("Expected validation error:")
    try:
        invalid_contact = AlienContact(
            contact_id="AC_BAD_002",
            timestamp=datetime.now(),
            location="Roswell",
            contact_type="telepathic",
            signal_strength=5.0,
            duration_minutes=10,
            witness_count=1,
            message_received=None,
            is_verified=False
        )
        print(invalid_contact)
    except ValidationError as e:
        for error in e.errors():
            msg = error['msg'].replace('Value error, ', '')
            print(f"{msg}")


if __name__ == "__main__":
    main()
