from rest_framework import serializers
from  employees.models import Employees,postion


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'

class postionSerializer(serializers.ModelSerializer):
    class Meta:
        model = postion
        fields = '__all__'
