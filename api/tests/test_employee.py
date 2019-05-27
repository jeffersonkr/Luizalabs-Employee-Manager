from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse, resolve
from core.models.Employee import Employee
from api.serializers.EmployeeSerializer import EmployeeSerializer

class GetAllEmployees(TestCase):
    """ Test module for GET all employees API """

    def setUp(self):
        Employee.objects.create(
            name='Casper', email='casper@gmail.com', department='E')
        Employee.objects.create(
            name='Joseph', email='joseph@gmail.com', department='M')

    def test_get_all_employees(self):
        client = Client()
        # get API response
        response = client.get(reverse('employees_list'))
        # get data from db
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)