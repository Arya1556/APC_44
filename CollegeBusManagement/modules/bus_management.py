from CollegeBusManagement.database import DATABASE_PATH, connect, transaction
from CollegeBusManagement.models.bus import Bus
from CollegeBusManagement.utils.validation import (
    positive_integer, require_text, validate_bus_number, validate_contact,
)


def add_bus(bus: Bus, database_path=DATABASE_PATH) -> int:
    capacity = positive_integer(str(bus.seating_capacity), "Seating capacity")
    with transaction(database_path) as connection:
        cursor = connection.execute(
            "INSERT INTO buses(bus_number, seating_capacity, driver_name, driver_contact, route_id) "
            "VALUES (?, ?, ?, ?, ?)",
            (validate_bus_number(bus.bus_number), capacity,
             require_text(bus.driver_name, "Driver name"),
             validate_contact(bus.driver_contact), bus.route_id),
        )
        return int(cursor.lastrowid)


def update_bus(bus_id: int, bus: Bus, database_path=DATABASE_PATH) -> None:
    capacity = positive_integer(str(bus.seating_capacity), "Seating capacity")
    with transaction(database_path) as connection:
        current = connection.execute("SELECT route_id FROM buses WHERE id=?", (bus_id,)).fetchone()
        if current is None:
            raise LookupError("Bus was not found.")
        occupied = connection.execute(
            "SELECT COUNT(*) FROM students WHERE bus_id=?", (bus_id,)
        ).fetchone()[0]
        if capacity < occupied:
            raise ValueError(f"Capacity cannot be below the {occupied} currently allocated seats.")
        if occupied and current["route_id"] != bus.route_id:
            raise ValueError("Reassign or remove this bus's students before changing its route.")
        cursor = connection.execute(
            "UPDATE buses SET bus_number=?, seating_capacity=?, driver_name=?, "
            "driver_contact=?, route_id=? WHERE id=?",
            (validate_bus_number(bus.bus_number), capacity,
             require_text(bus.driver_name, "Driver name"),
             validate_contact(bus.driver_contact), bus.route_id, bus_id),
        )


def delete_bus(bus_id: int, database_path=DATABASE_PATH) -> None:
    with transaction(database_path) as connection:
        connection.execute(
            "UPDATE students SET bus_id=NULL, seat_number=NULL WHERE bus_id=?", (bus_id,)
        )
        cursor = connection.execute("DELETE FROM buses WHERE id=?", (bus_id,))
        if not cursor.rowcount:
            raise LookupError("Bus was not found.")


def list_buses(database_path=DATABASE_PATH, search: str = "") -> list:
    search_term = f"%{search.strip()}%"
    with connect(database_path) as connection:
        return connection.execute(
            "SELECT b.*, r.route_name, COUNT(s.seat_number) AS occupied_seats, "
            "b.seating_capacity-COUNT(s.seat_number) AS available_seats, "
            "CASE WHEN b.seating_capacity-COUNT(s.seat_number) <= 0 "
            "THEN 'Full' ELSE 'Available' END AS bus_status "
            "FROM buses b LEFT JOIN routes r ON r.id=b.route_id "
            "LEFT JOIN students s ON s.bus_id=b.id AND s.seat_number IS NOT NULL "
            "WHERE ?='' OR b.bus_number LIKE ? OR b.driver_name LIKE ? OR r.route_name LIKE ? "
            "GROUP BY b.id ORDER BY b.bus_number",
            (search.strip(), search_term, search_term, search_term),
        ).fetchall()


def get_bus(bus_id: int, database_path=DATABASE_PATH):
    with connect(database_path) as connection:
        result = connection.execute("SELECT * FROM buses WHERE id=?", (bus_id,)).fetchone()
    if result is None:
        raise LookupError("Bus was not found.")
    return result


def get_bus_details(bus_id: int, database_path=DATABASE_PATH):
    with connect(database_path) as connection:
        result = connection.execute(
            "SELECT b.*, r.route_name, COUNT(s.seat_number) AS occupied_seats, "
            "b.seating_capacity-COUNT(s.seat_number) AS available_seats "
            "FROM buses b LEFT JOIN routes r ON r.id=b.route_id "
            "LEFT JOIN students s ON s.bus_id=b.id AND s.seat_number IS NOT NULL "
            "WHERE b.id=? GROUP BY b.id",
            (bus_id,),
        ).fetchone()
    if result is None:
        raise LookupError("Bus was not found.")
    return result


def get_bus_seating(bus_id: int, database_path=DATABASE_PATH) -> list[dict]:
    details = get_bus_details(bus_id, database_path)
    with connect(database_path) as connection:
        occupied = {
            row["seat_number"]: {
                "name": row["name"],
                "roll_number": row["roll_number"],
            }
            for row in connection.execute(
                "SELECT seat_number, name, roll_number FROM students "
                "WHERE bus_id=? AND seat_number IS NOT NULL",
                (bus_id,),
            )
        }
    return [
        {
            "seat_number": seat_number,
            "occupied": seat_number in occupied,
            "student": occupied.get(seat_number),
        }
        for seat_number in range(1, details["seating_capacity"] + 1)
    ]
