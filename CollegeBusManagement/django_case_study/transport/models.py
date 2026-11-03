from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=80)
    year = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f"{self.roll_number} - {self.name}"
