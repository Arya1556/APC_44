from dataclasses import dataclass


@dataclass
class Student:
    name: str
    roll_number: str
    department: str
    year: int
    contact_number: str
    bus_id: int | None = None
    route_id: int | None = None
    pickup_stop_id: int | None = None
    seat_number: int | None = None

    def transport_summary(self, include_contact: bool = False) -> str:
        details = f"{self.roll_number}: {self.name}"
        if include_contact:
            details += f" ({self.contact_number})"
        return details
