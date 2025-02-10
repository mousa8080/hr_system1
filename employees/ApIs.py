from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import *
from .models import Employees,postion
from employees.serializer import EmployeesSerializer,postionSerializer

class EmployeesCreateListView(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer


class EmployeesDetailsAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    
class ExampleApi(APIView):

    """
    GET-->    api/emplyees/ list of employees
    POST --> api/emplyees/ {emplyee} 200 , {}
    GET --> api/emplyees/<int:id> one emplyee
    PUT , patch -->api/emplyees/<int:id>
    DELETE --> api/emplyees/<int:id>

    
    
    """
    def get(self, request):
        return Response({'hello': 'world'})
    def post(self, request):
        return Response({'hello': 'world'})
    def put(self, request):
        return Response({'hello': 'world'})
    def patch(self, request):
        return Response({'hello': 'world'})
    def delete(self, request):
        return Response({'hello': 'world'})

class postionApiView(generics.ListCreateAPIView):
    queryset = postion.objects.all()
    queryset = postion.objects.all().delete()
    serializer_class = postionSerializer

