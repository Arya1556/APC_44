from CollegeBusManagement.database import DATABASE_PATH, connect, transaction
from CollegeBusManagement.models.student import Student
from CollegeBusManagement.utils.validation import (
    positive_integer, require_text, validate_contact, validate_roll_number,
)


def _assignment(connection, bus_id, route_id, stop_id, seat_number, current_student_id=None):
    if bus_id is None:
        if seat_number is not None:
            raise ValueError("A seat cannot be assigned without a bus.")
        if route_id is not None and not connection.execute(
            "SELECT 1 FROM routes WHERE id=?", (route_id,)
        ).fetchone():
            raise LookupError("Selected route was not found.")
        if stop_id is not None:
            stop = connection.execute(
                "SELECT route_id FROM stops WHERE id=?", (stop_id,)
            ).fetchone()
            if stop is None or stop["route_id"] != route_id:
                raise ValueError("Pickup stop must belong to the student's assigned route.")
        return None, route_id, stop_id, None
    bus = connection.execute("SELECT * FROM buses WHERE id=?", (bus_id,)).fetchone()
    if bus is None:
        raise LookupError("Selected bus was not found.")
    if route_id is None:
        route_id = bus["route_id"]
    if route_id is None or bus["route_id"] != route_id:
        raise ValueError("The selected bus must be assigned to the student's route.")
    if stop_id is not None:
        stop = connection.execute(
            "SELECT route_id FROM stops WHERE id=?", (stop_id,)
        ).fetchone()
        if stop is None or stop["route_id"] != route_id:
            raise ValueError("Pickup stop must belong to the student's assigned route.")
    if seat_number is None:
        occupied = {
            row[0] for row in connection.execute(
                "SELECT seat_number FROM students WHERE bus_id=? AND id != COALESCE(?, -1)",
                (bus_id, current_student_id),
            )
        }
        seat_number = next(
            (seat for seat in range(1, bus["seating_capacity"] + 1) if seat not in occupied),
            None,
        )
        if seat_number is None:
            raise ValueError("The selected bus is full.")
    else:
        seat_number = positive_integer(str(seat_number), "Seat number")
        if seat_number > bus["seating_capacity"]:
            raise ValueError("Seat number exceeds the bus seating capacity.")
        conflict = connection.execute(
            "SELECT 1 FROM students WHERE bus_id=? AND seat_number=? AND id != COALESCE(?, -1)",
            (bus_id, seat_number, current_student_id),
        ).fetchone()
        if conflict:
            raise ValueError("That seat is already occupied on this bus.")
    return bus_id, route_id, stop_id, seat_number


def _insert_student(connection, student: Student) -> int:
    assignment = _assignment(
        connection, student.bus_id, student.route_id, student.pickup_stop_id, student.seat_number
    )
    cursor = connection.execute(
        "INSERT INTO students(name, roll_number, department, year, contact_number, "
        "bus_id, route_id, pickup_stop_id, seat_number) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (require_text(student.name, "Name"), validate_roll_number(student.roll_number),
         require_text(student.department, "Department"),
         positive_integer(str(student.year), "Year"), validate_contact(student.contact_number),
         *assignment),
    )
    return int(cursor.lastrowid)


def add_student(student: Student, database_path=DATABASE_PATH) -> int:
    with transaction(database_path) as connection:
        return _insert_student(connection, student)


def update_student(student_id: int, student: Student, database_path=DATABASE_PATH) -> None:
    with transaction(database_path) as connection:
        assignment = _assignment(
            connection, student.bus_id, student.route_id, student.pickup_stop_id,
            student.seat_number, student_id,
        )
        cursor = connection.execute(
            "UPDATE students SET name=?, roll_number=?, department=?, year=?, contact_number=?, "
            "bus_id=?, route_id=?, pickup_stop_id=?, seat_number=? WHERE id=?",
            (require_text(student.name, "Name"), validate_roll_number(student.roll_number),
             require_text(student.department, "Department"),
             positive_integer(str(student.year), "Year"), validate_contact(student.contact_number),
             *assignment, student_id),
        )
        if not cursor.rowcount:
            raise LookupError("Student was not found.")


def delete_student(student_id: int, database_path=DATABASE_PATH) -> None:
    with transaction(database_path) as connection:
        cursor = connection.execute("DELETE FROM students WHERE id=?", (student_id,))
        if not cursor.rowcount:
            raise LookupError("Student was not found.")


def list_students(search: str = "", database_path=DATABASE_PATH) -> list:
    pattern = f"%{search.strip()}%"
    with connect(database_path) as connection:
        return connection.execute(
            "SELECT s.*, b.bus_number, r.route_name, st.stop_name AS pickup_stop "
            "FROM students s LEFT JOIN buses b ON b.id=s.bus_id "
            "LEFT JOIN routes r ON r.id=s.route_id LEFT JOIN stops st ON st.id=s.pickup_stop_id "
            "WHERE ?='' OR s.name LIKE ? OR s.roll_number LIKE ? OR b.bus_number LIKE ? "
            "OR r.route_name LIKE ? ORDER BY s.name",
            (search.strip(), pattern, pattern, pattern, pattern),
        ).fetchall()


def import_student_records(rows: list[dict], database_path=DATABASE_PATH) -> int:
    count = 0
    with transaction(database_path) as connection:
        for row in rows:
            bus = row.get("bus_number", "").strip()
            route = row.get("route_name", "").strip()
            stop = row.get("pickup_stop", "").strip()
            bus_row = connection.execute(
                "SELECT id FROM buses WHERE bus_number=?", (bus,)
            ).fetchone() if bus else None
            route_row = connection.execute(
                "SELECT id FROM routes WHERE route_name=?", (route,)
            ).fetchone() if route else None
            if bus and bus_row is None:
                raise LookupError(f"Bus number {bus!r} from the CSV was not found.")
            if route and route_row is None:
                raise LookupError(f"Route {route!r} from the CSV was not found.")
            if bus_row and route_row is None:
                route_row = connection.execute(
                    "SELECT route_id AS id FROM buses WHERE id=?", (bus_row["id"],)
                ).fetchone()
            stop_row = connection.execute(
                "SELECT id FROM stops WHERE route_id=? AND stop_name=?",
                (route_row["id"], stop),
            ).fetchone() if route_row and stop else None
            if stop and stop_row is None:
                raise LookupError(f"Pickup stop {stop!r} from the CSV was not found on that route.")
            _insert_student(
                connection,
                Student(
                    name=row["name"], roll_number=row["roll_number"], department=row["department"],
                    year=int(row["year"]), contact_number=row["contact_number"],
                    bus_id=bus_row["id"] if bus_row else None,
                    route_id=route_row["id"] if route_row else None,
                    pickup_stop_id=stop_row["id"] if stop_row else None,
                    seat_number=int(row["seat_number"]) if row.get("seat_number", "").strip() else None,
                ),
            )
            count += 1
    return count
