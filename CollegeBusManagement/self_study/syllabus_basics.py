"""Small examples for Python structures and method-dispatch syllabus topics."""

from CollegeBusManagement.models.bus import Bus
from CollegeBusManagement.models.staff import Admin, TransportStaff


def demonstrate_basics() -> dict:
    student_record = {"name": "Asha", "department": "Science", "year": 1}
    route_stops = ["Library", "Main Street", "College"]
    fixed_years = (1, 2, 3, 4)
    unique_departments = {"Science", "Arts", "Science"}
    sorted_stops = sorted(route_stops, key=lambda stop: stop.lower())
    staff: list[TransportStaff] = [
        TransportStaff("Driver", "9876543210"),
        Admin("Office Admin", "9876543211"),
    ]
    return {
        "record": student_record,
        "stops": route_stops,
        "fixed_years": fixed_years,
        "departments": unique_departments,
        "sorted_stops": sorted_stops,
        "staff_summaries": [member.role_summary() for member in staff],
        "available_seats": Bus("BUS-EXAMPLE", 40, "Driver", "9876543210").available_seats(12),
    }


if __name__ == "__main__":
    print(demonstrate_basics())
