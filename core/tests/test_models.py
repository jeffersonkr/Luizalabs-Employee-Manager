from core.models.Employee import Employee
from django.db.utils import IntegrityError
import pytest

@pytest.mark.django_db 
class TestEmployee:
    """Test for employee models."""

    def test_register_employee(self):
        """test registering employee."""
        
        employee = Employee.objects.create(
            name = 'Test',
            email = 'test2@email.com',
            department = 'M'
        )
        assert Employee.objects.get(email='test2@email.com') == employee