from enum import Enum
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, model_validator, ValidationError


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
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
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')

        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError('Physical contact reports must be verified')

        if self.contact_type == ContactType.telepathic and self.witness_count < 3:
            raise ValueError('Telepathic contact requires at least 3 witnesses')

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError('Strong signals (> 7.0) should include received messages')

        return self

def main():
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
    except ValidationError as e:
        for error in e.errors():
            msg = error['msg'].replace('Value error, ', '')
            print(f"{msg}")

if __name__ == "__main__":
    main()