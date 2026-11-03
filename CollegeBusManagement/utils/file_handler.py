import csv
from pathlib import Path


STUDENT_FIELDS = (
    "name", "roll_number", "department", "year", "contact_number",
    "bus_number", "route_name", "pickup_stop", "seat_number",
)


def export_students(rows: list[dict], path: str | Path) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=STUDENT_FIELDS)
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in STUDENT_FIELDS} for row in rows)


def import_students(path: str | Path) -> list[dict]:
    source = Path(path)
    try:
        csv_file = source.open("r", newline="", encoding="utf-8-sig")
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"CSV file was not found: {source}") from exc
    else:
        with csv_file:
            reader = csv.DictReader(csv_file)
            if not reader.fieldnames or not set(STUDENT_FIELDS).issubset(reader.fieldnames):
                raise ValueError("CSV must include these columns: " + ", ".join(STUDENT_FIELDS))
            return [dict(row) for row in reader]
