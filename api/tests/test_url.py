import json
from rest_framework import status
from django.urls import reverse, resolve
from django.test import TestCase, Client
from core.models.Employee import Employee
from api.serializers.EmployeeSerializer import EmployeeSerializer


class TestUrls:
"""Testing url path and url name"""

    def test_employees_list(self):
        path = reverse('employees_list')
        assert resolve(path).view_name == 'employees_list'


class GetAllEmployees(TestCase):
    """ Test module for GET all employees API """

    def setUp(self):
        Employee.objects.create(
            name='Casper', email='casper@gmail.com', department='E')

    def test_get_all_employees(self):
        client = Client()
        # get API response
        response = client.get(reverse('employees_list'))
        # get data from db
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)