import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator


DATABASE_PATH = Path(__file__).resolve().parent / "college_bus.db"


class ClosingConnection(sqlite3.Connection):
    def __exit__(self, exc_type, exc_value, traceback):
        try:
            return super().__exit__(exc_type, exc_value, traceback)
        finally:
            self.close()


def connect(database_path: str | Path = DATABASE_PATH) -> sqlite3.Connection:
    connection = sqlite3.connect(database_path, factory=ClosingConnection)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


@contextmanager
def transaction(database_path: str | Path = DATABASE_PATH) -> Iterator[sqlite3.Connection]:
    connection = connect(database_path)
    try:
        connection.execute("BEGIN IMMEDIATE")
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def initialize_database(database_path: str | Path = DATABASE_PATH) -> None:
    with connect(database_path) as connection:
        connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS routes (
                id INTEGER PRIMARY KEY,
                route_name TEXT NOT NULL UNIQUE,
                starting_point TEXT NOT NULL,
                destination TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS stops (
                id INTEGER PRIMARY KEY,
                route_id INTEGER NOT NULL REFERENCES routes(id) ON DELETE CASCADE,
                stop_name TEXT NOT NULL,
                stop_order INTEGER NOT NULL CHECK (stop_order > 0),
                UNIQUE(route_id, stop_order),
                UNIQUE(route_id, stop_name)
            );
            CREATE TABLE IF NOT EXISTS buses (
                id INTEGER PRIMARY KEY,
                bus_number TEXT NOT NULL UNIQUE,
                seating_capacity INTEGER NOT NULL CHECK (seating_capacity > 0),
                driver_name TEXT NOT NULL,
                driver_contact TEXT NOT NULL,
                route_id INTEGER REFERENCES routes(id) ON DELETE SET NULL
            );
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                roll_number TEXT NOT NULL UNIQUE,
                department TEXT NOT NULL,
                year INTEGER NOT NULL CHECK (year > 0),
                contact_number TEXT NOT NULL,
                bus_id INTEGER REFERENCES buses(id) ON DELETE SET NULL,
                route_id INTEGER REFERENCES routes(id) ON DELETE SET NULL,
                pickup_stop_id INTEGER REFERENCES stops(id) ON DELETE SET NULL,
                seat_number INTEGER CHECK (seat_number IS NULL OR seat_number > 0),
                CHECK ((bus_id IS NULL AND seat_number IS NULL) OR
                       (bus_id IS NOT NULL AND seat_number IS NOT NULL)),
                UNIQUE(bus_id, seat_number)
            );
            CREATE TABLE IF NOT EXISTS fees (
                id INTEGER PRIMARY KEY,
                student_id INTEGER NOT NULL REFERENCES students(id) ON DELETE CASCADE,
                total_fee REAL NOT NULL CHECK (total_fee >= 0),
                amount_paid REAL NOT NULL DEFAULT 0 CHECK (amount_paid >= 0 AND amount_paid <= total_fee),
                payment_date TEXT NOT NULL DEFAULT CURRENT_DATE
            );
            CREATE TABLE IF NOT EXISTS admins (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL COLLATE NOCASE UNIQUE,
                password_salt BLOB NOT NULL,
                password_hash BLOB NOT NULL,
                hash_iterations INTEGER NOT NULL CHECK (hash_iterations >= 100000),
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
            """
        )


def seed_sample_data(database_path: str | Path = DATABASE_PATH) -> None:
    with transaction(database_path) as connection:
        if connection.execute("SELECT COUNT(*) FROM routes").fetchone()[0]:
            return
        route_id = connection.execute(
            "INSERT INTO routes(route_name, starting_point, destination) VALUES (?, ?, ?)",
            ("North Campus", "Central Station", "College"),
        ).lastrowid
        connection.executemany(
            "INSERT INTO stops(route_id, stop_name, stop_order) VALUES (?, ?, ?)",
            [(route_id, "Central Station", 1), (route_id, "City Library", 2)],
        )
        connection.execute(
            "INSERT INTO buses(bus_number, seating_capacity, driver_name, driver_contact, route_id) "
            "VALUES (?, ?, ?, ?, ?)",
            ("BUS-01", 30, "Sample Driver", "9876543210", route_id),
        )
