from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from api.serializers.EmployeeSerializer import EmployeeSerializer
from core.models.Employee import Employee


"""
from rest_framework import viewsets

class EmployeeViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows users to be viewed or edited.
    '''
    queryset = Employee.objects.all().order_by('name')
    serializer_class = EmployeeSerializer
"""

@api_view(['GET'])
def employees_list(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def employee_register(request):
    data = JSONParser().parse(request)
    employee = EmployeeSerializer(data=data)
    if employee.is_valid():
        employee.save()
    return JsonResponse(employee.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes((IsAuthenticated, ))
def employee_details(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        employee = EmployeeSerializer(employee)
        return JsonResponse(employee.data)

    elif request.method == "DELETE":
        employee.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        employee = EmployeeSerializer(employee, data=data)
        if employee.is_valid():
            employee.save()
        return JsonResponse(employee.errors, status=status.HTTP_400_BAD_REQUEST)
    