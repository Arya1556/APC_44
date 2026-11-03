import tempfile
import unittest
from pathlib import Path

from CollegeBusManagement.database import connect, initialize_database
from CollegeBusManagement.models.bus import Bus
from CollegeBusManagement.models.fee import Fee
from CollegeBusManagement.models.route import Route
from CollegeBusManagement.models.student import Student
from CollegeBusManagement.modules.bus_management import (
    add_bus, delete_bus, get_bus_details, get_bus_seating, list_buses, update_bus,
)
from CollegeBusManagement.modules.fee_management import add_fee, fee_totals
from CollegeBusManagement.modules.route_management import add_route, add_stop, delete_route
from CollegeBusManagement.modules.seat_allocation import seating_chart
from CollegeBusManagement.modules.student_management import (
    add_student, import_student_records, list_students, update_student,
)
from CollegeBusManagement.utils.file_handler import export_students, import_students


class CoreWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.database = Path(self.temporary.name) / "test.db"
        initialize_database(self.database)
        self.route_id = add_route(Route("Route A", "Town", "College"), self.database)
        self.stop_id = add_stop(self.route_id, "Main Street", 1, self.database)
        self.bus_id = add_bus(
            Bus("BUS-01", 2, "Driver", "9876543210", self.route_id), self.database
        )

    def tearDown(self):
        self.temporary.cleanup()

    def test_lowest_available_seat_and_capacity(self):
        first = Student("A Student", "A-01", "Science", 1, "9876543210",
                        self.bus_id, self.route_id, self.stop_id)
        second = Student("B Student", "B-02", "Arts", 2, "9876543211",
                         self.bus_id, self.route_id, self.stop_id)
        add_student(first, self.database)
        add_student(second, self.database)
        chart = seating_chart(self.bus_id, self.database)
        self.assertEqual([item["seat_number"] for item in chart], [1, 2])
        self.assertTrue(all(item["occupied"] for item in chart))
        with self.assertRaisesRegex(ValueError, "full"):
            add_student(
                Student("C Student", "C-03", "Arts", 2, "9876543212",
                        self.bus_id, self.route_id, self.stop_id),
                self.database,
            )

    def test_seat_number_may_repeat_on_another_bus(self):
        second_bus = add_bus(
            Bus("BUS-02", 1, "Other Driver", "9876543212", self.route_id), self.database
        )
        for name, roll, bus_id in (
            ("A Student", "A-01", self.bus_id),
            ("B Student", "B-02", second_bus),
        ):
            add_student(
                Student(name, roll, "Science", 1, "9876543210",
                        bus_id, self.route_id, self.stop_id, 1),
                self.database,
            )

    def test_assignment_change_releases_old_seat(self):
        student_id = add_student(
            Student("A Student", "A-01", "Science", 1, "9876543210",
                    self.bus_id, self.route_id, self.stop_id),
            self.database,
        )
        update_student(
            student_id,
            Student("A Student", "A-01", "Science", 1, "9876543210"),
            self.database,
        )
        self.assertFalse(any(item["occupied"] for item in seating_chart(self.bus_id, self.database)))

    def test_route_only_assignment_is_kept(self):
        student_id = add_student(
            Student("Route Student", "R-01", "Science", 1, "9876543210",
                    route_id=self.route_id, pickup_stop_id=self.stop_id),
            self.database,
        )
        with connect(self.database) as connection:
            row = connection.execute(
                "SELECT route_id, pickup_stop_id, bus_id FROM students WHERE id=?",
                (student_id,),
            ).fetchone()
        self.assertEqual(row["route_id"], self.route_id)
        self.assertEqual(row["pickup_stop_id"], self.stop_id)
        self.assertIsNone(row["bus_id"])

    def test_route_deletion_releases_students_bus_seats(self):
        add_student(
            Student("A Student", "A-01", "Science", 1, "9876543210",
                    self.bus_id, self.route_id, self.stop_id),
            self.database,
        )
        delete_route(self.route_id, self.database)
        with connect(self.database) as connection:
            row = connection.execute(
                "SELECT bus_id, route_id, seat_number, pickup_stop_id FROM students"
            ).fetchone()
        self.assertEqual(tuple(row), (None, None, None, None))

    def test_fee_totals_and_csv_round_trip(self):
        student_id = add_student(
            Student("A Student", "A-01", "Science", 1, "9876543210"),
            self.database,
        )
        add_fee(Fee(student_id, 1000, 250), self.database)
        self.assertEqual(fee_totals(self.database), {"collected": 250.0, "outstanding": 750.0})
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "students.csv"
            export_students([dict(list_students(database_path=self.database)[0])], path)
            rows = import_students(path)
        self.assertEqual(rows[0]["roll_number"], "A-01")
        self.assertEqual(rows[0]["name"], "A Student")

    def test_invalid_csv_reference_rolls_back_the_import(self):
        rows = [
            {
                "name": "Valid Student", "roll_number": "V-01", "department": "Science",
                "year": "1", "contact_number": "9876543210", "bus_number": "",
                "route_name": "", "pickup_stop": "", "seat_number": "",
            },
            {
                "name": "Invalid Student", "roll_number": "I-02", "department": "Arts",
                "year": "1", "contact_number": "9876543211", "bus_number": "MISSING",
                "route_name": "", "pickup_stop": "", "seat_number": "",
            },
        ]
        with self.assertRaisesRegex(LookupError, "was not found"):
            import_student_records(rows, self.database)
        self.assertEqual(list_students(database_path=self.database), [])

    def test_bus_occupancy_is_calculated_from_allocated_seats(self):
        add_student(
            Student("Assigned Student", "A-10", "Science", 1, "9876543210",
                    self.bus_id, self.route_id, self.stop_id),
            self.database,
        )
        bus = list_buses(search="BUS-01", database_path=self.database)[0]
        self.assertEqual(bus["occupied_seats"], 1)
        self.assertEqual(bus["available_seats"], 1)
        self.assertEqual(bus["bus_status"], "Available")
        self.assertEqual(list_buses(search="No match", database_path=self.database), [])
        details = get_bus_details(self.bus_id, self.database)
        self.assertEqual(details["occupied_seats"], 1)
        seats = get_bus_seating(self.bus_id, self.database)
        self.assertEqual(seats[0]["student"]["roll_number"], "A-10")
        self.assertFalse(seats[1]["occupied"])
        second_student_id = add_student(
            Student("Second Student", "A-11", "Science", 1, "9876543211",
                    self.bus_id, self.route_id, self.stop_id),
            self.database,
        )
        full_bus = list_buses(database_path=self.database)[0]
        self.assertEqual(full_bus["occupied_seats"], 2)
        self.assertEqual(full_bus["available_seats"], 0)
        self.assertEqual(full_bus["bus_status"], "Full")
        with self.assertRaisesRegex(ValueError, "Capacity cannot be below"):
            update_bus(
                self.bus_id, Bus("BUS-01", 1, "Driver", "9876543210", self.route_id),
                self.database,
            )

    def test_database_initialization_preserves_existing_records(self):
        add_student(
            Student("Existing Student", "EX-01", "Science", 1, "9876543210",
                    self.bus_id, self.route_id, self.stop_id),
            self.database,
        )
        initialize_database(self.database)
        with connect(self.database) as connection:
            student_count = connection.execute("SELECT COUNT(*) FROM students").fetchone()[0]
            tables = {
                row[0] for row in connection.execute(
                    "SELECT name FROM sqlite_master WHERE type='table'"
                )
            }
        self.assertEqual(student_count, 1)
        self.assertIn("admins", tables)

    def test_deleting_bus_releases_allocation_without_deleting_student(self):
        student_id = add_student(
            Student("Kept Student", "KEEP-01", "Science", 1, "9876543210",
                    self.bus_id, self.route_id, self.stop_id),
            self.database,
        )
        delete_bus(self.bus_id, self.database)
        with connect(self.database) as connection:
            student = connection.execute(
                "SELECT bus_id, seat_number FROM students WHERE id=?", (student_id,)
            ).fetchone()
        self.assertIsNone(student["bus_id"])
        self.assertIsNone(student["seat_number"])
        self.assertEqual(list_buses(database_path=self.database), [])


if __name__ == "__main__":
    unittest.main()
