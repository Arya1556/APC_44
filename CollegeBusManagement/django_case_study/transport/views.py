import json

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.db import IntegrityError

from transport.models import Student


def _required_text(data: dict, field: str) -> str:
    value = data[field]
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a non-empty string.")
    return value.strip()


def _student_data(student: Student) -> dict:
    return {
        "id": student.id,
        "name": student.name,
        "roll_number": student.roll_number,
        "department": student.department,
        "year": student.year,
    }


def student_collection(request):
    if request.method == "GET":
        return JsonResponse([_student_data(student) for student in Student.objects.all()], safe=False)
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            student = Student(
                name=_required_text(data, "name"),
                roll_number=_required_text(data, "roll_number"),
                department=_required_text(data, "department"),
                year=int(data["year"]),
            )
            student.full_clean()
            student.save()
        except (json.JSONDecodeError, KeyError, TypeError, ValueError,
                ValidationError, IntegrityError) as error:
            return JsonResponse({"error": f"Invalid student data: {error}"}, status=400)
        return JsonResponse(_student_data(student), status=201)
    return JsonResponse({"error": "Use GET or POST."}, status=405)


def student_detail(request, student_id: int):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        return JsonResponse({"error": "Student was not found."}, status=404)
    if request.method == "GET":
        return JsonResponse(_student_data(student))
    if request.method in ("PUT", "PATCH"):
        try:
            data = json.loads(request.body)
            for field in ("name", "roll_number", "department"):
                if field in data:
                    setattr(student, field, _required_text(data, field))
            if "year" in data:
                student.year = int(data["year"])
            student.full_clean()
            student.save()
        except (json.JSONDecodeError, TypeError, ValueError, ValidationError, IntegrityError) as error:
            return JsonResponse({"error": str(error)}, status=400)
        return JsonResponse(_student_data(student))
    if request.method == "DELETE":
        student.delete()
        return JsonResponse({"deleted": True})
    return JsonResponse({"error": "Use GET, PUT, PATCH, or DELETE."}, status=405)
