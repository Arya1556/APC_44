from CollegeBusManagement.database import DATABASE_PATH, transaction


def lowest_available_seat(bus_id: int, database_path=DATABASE_PATH) -> int:
    with transaction(database_path) as connection:
        bus = connection.execute(
            "SELECT seating_capacity FROM buses WHERE id=?", (bus_id,)
        ).fetchone()
        if bus is None:
            raise LookupError("Bus was not found.")
        occupied = {
            row[0] for row in connection.execute(
                "SELECT seat_number FROM students WHERE bus_id=?", (bus_id,)
            )
        }
        for seat in range(1, bus["seating_capacity"] + 1):
            if seat not in occupied:
                return seat
        raise ValueError("The selected bus is full.")


def seating_chart(bus_id: int, database_path=DATABASE_PATH) -> list[dict]:
    with transaction(database_path) as connection:
        bus = connection.execute(
            "SELECT seating_capacity FROM buses WHERE id=?", (bus_id,)
        ).fetchone()
        if bus is None:
            raise LookupError("Bus was not found.")
        occupied = {
            row["seat_number"]: row["name"]
            for row in connection.execute(
                "SELECT seat_number, name FROM students WHERE bus_id=?", (bus_id,)
            )
        }
        return [
            {"seat_number": seat, "occupied": seat in occupied, "student": occupied.get(seat)}
            for seat in range(1, bus["seating_capacity"] + 1)
        ]
