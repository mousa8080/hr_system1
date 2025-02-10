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
    
class postionApiView(generics.ListCreateAPIView):
    queryset = postion.objects.all()
    serializer_class = postionSerializer

