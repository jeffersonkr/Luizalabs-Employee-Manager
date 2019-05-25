from django.db import models
from .Person import Person

class Employee(Person):
    """Employee model."""

    DEPARTMENT_CHOICES = [
        ('A', 'Architeture'),
        ('E', 'E-commerce'),
        ('M', 'Mobile'),
    ]

    department = models.CharField(max_length=25, choices=DEPARTMENT_CHOICES)

    class Meta:
        managed = True
        db_table = 'Employee'
        verbose_name_plural = 'Employees'