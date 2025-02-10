from rest_framework import generics,viewsets
from .models import Branches,Department
from .serializers import BranchesSerializer
from .serializers import DepartmentSerializer


class BranchListCreate(generics.ListCreateAPIView):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer

class BrancheDetailsAPI(generics.RetrieveAPIView):
    queryset=Branches.objects.all()
    serializer_class = BranchesSerializer

class departmenttCreate(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class departmentDetailsAPI(generics.RetrieveAPIView):
    queryset=Department.objects.all()
    serializer_class = DepartmentSerializer



