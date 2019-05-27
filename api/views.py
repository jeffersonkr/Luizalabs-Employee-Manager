from django.http import Http404
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models.Employee import Employee
from core.models import Employee
from api.serializers.EmployeeSerializer import EmployeeSerializer


class EmployeeList(APIView):
    '''List all employees, or create a new employee.'''

    def get(self, request, format=None):
        """List all employees"""

        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """Create a new employee"""

        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetail(APIView):
    """Retrieve, update or delete an employee instance."""

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get_object(self, pk):
        try:
            print(pk)
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)