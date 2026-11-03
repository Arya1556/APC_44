from pathlib import Path

import numpy as np
import pandas as pd

from CollegeBusManagement.database import DATABASE_PATH, connect
from CollegeBusManagement.modules.fee_management import fee_totals


def dashboard_summary(database_path=DATABASE_PATH) -> dict:
    with connect(database_path) as connection:
        counts = connection.execute(
            "SELECT (SELECT COUNT(*) FROM students) AS students, "
            "(SELECT COUNT(*) FROM buses) AS buses, (SELECT COUNT(*) FROM routes) AS routes, "
            "(SELECT COALESCE(SUM(seating_capacity), 0) FROM buses) AS capacity, "
            "(SELECT COUNT(*) FROM students WHERE bus_id IS NOT NULL) AS occupied"
        ).fetchone()
        bus_occupancy = np.array(
            [row["occupied"] for row in connection.execute(
                "SELECT b.id, COUNT(s.id) AS occupied FROM buses b "
                "LEFT JOIN students s ON s.bus_id=b.id GROUP BY b.id"
            )],
            dtype=int,
        )
        route_rows = connection.execute(
            "SELECT r.route_name, COUNT(s.id) AS students FROM routes r "
            "LEFT JOIN students s ON s.route_id=r.id GROUP BY r.id ORDER BY r.route_name"
        ).fetchall()
    totals = fee_totals(database_path)
    return {
        "students": counts["students"],
        "buses": counts["buses"],
        "routes": counts["routes"],
        "occupied_seats": int(bus_occupancy.sum()),
        "vacant_seats": int(counts["capacity"] - counts["occupied"]),
        "fees_collected": totals["collected"],
        "fees_outstanding": totals["outstanding"],
        "route_students": pd.DataFrame([dict(row) for row in route_rows]),
    }


def student_dataframe(database_path=DATABASE_PATH) -> pd.DataFrame:
    with connect(database_path) as connection:
        return pd.read_sql_query(
            "SELECT s.name, s.roll_number, s.department, s.year, s.contact_number, "
            "b.bus_number, r.route_name, st.stop_name AS pickup_stop, s.seat_number "
            "FROM students s LEFT JOIN buses b ON b.id=s.bus_id "
            "LEFT JOIN routes r ON r.id=s.route_id "
            "LEFT JOIN stops st ON st.id=s.pickup_stop_id ORDER BY s.name",
            connection,
        )


def export_chart(path: str | Path, database_path=DATABASE_PATH) -> Path:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    with connect(database_path) as connection:
        rows = connection.execute(
            "SELECT b.bus_number, b.seating_capacity, COUNT(s.id) AS occupied "
            "FROM buses b LEFT JOIN students s ON s.bus_id=b.id GROUP BY b.id ORDER BY b.bus_number"
        ).fetchall()
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    names = [row["bus_number"] for row in rows]
    occupied = [row["occupied"] for row in rows]
    capacity = [row["seating_capacity"] for row in rows]
    positions = np.arange(len(names))
    figure, axis = plt.subplots()
    axis.bar(positions, capacity, label="Capacity")
    axis.bar(positions, occupied, label="Occupied")
    axis.set_xticks(positions, names)
    axis.set_ylabel("Seats")
    axis.set_title("Bus occupancy")
    axis.legend()
    figure.tight_layout()
    figure.savefig(destination)
    plt.close(figure)
    return destination


def export_fee_chart(path: str | Path, database_path=DATABASE_PATH) -> Path:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    with connect(database_path) as connection:
        rows = connection.execute(
            "SELECT COALESCE(SUM(amount_paid), 0) AS collected, "
            "COALESCE(SUM(total_fee-amount_paid), 0) AS outstanding FROM fees"
        ).fetchone()
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    figure, axis = plt.subplots()
    axis.bar(["Collected", "Outstanding"], [rows["collected"], rows["outstanding"]],
             color=["#69a96b", "#d98b4c"])
    axis.set_ylabel("Amount")
    axis.set_title("Transport fee summary")
    figure.tight_layout()
    figure.savefig(destination)
    plt.close(figure)
    return destination
