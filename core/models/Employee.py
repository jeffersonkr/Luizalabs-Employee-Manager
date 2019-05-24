from django.db import models
from .Person import Person

class Employee(Person):
    """Employee model."""

    DEPARTMENT_CHOICES = [
        ('Architeture', 'Architeture'),
        ('E-commerce', 'E-commerce'),
        ('Mobile', 'Mobile'),
    ]

    department = models.CharField(max_length=25, choices=DEPARTMENT_CHOICES)

    class Meta:
        managed = True
        db_table = 'Employee'
        verbose_name_plural = 'Employees'