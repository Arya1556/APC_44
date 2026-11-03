from dataclasses import dataclass


@dataclass
class Bus:
    bus_number: str
    seating_capacity: int
    driver_name: str
    driver_contact: str
    route_id: int | None = None

    def available_seats(self, occupied: int = 0) -> int:
        return max(0, self.seating_capacity - occupied)
