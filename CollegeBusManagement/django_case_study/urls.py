from django.urls import path

from transport.views import student_collection, student_detail


urlpatterns = [
    path("api/students/", student_collection, name="student_collection"),
    path("api/students/<int:student_id>/", student_detail, name="student_detail"),
]
