from django.urls import path
from company import views
from company.APIs import BranchListCreate,BrancheDetailsAPI,departmenttCreate,departmentDetailsAPI

urlpatterns = [



    path('API/BranchesList',BranchListCreate.as_view(),name="BranchListCreate"),
    path('API/Branchesdetails/<int:pk>',BrancheDetailsAPI.as_view(),name="BrancheDetails"),
    path('API/departmentList',departmenttCreate.as_view(),name="departmenttCreate"),
    path('API/departmentdetails/<int:pk>',departmentDetailsAPI.as_view(),name="departmentDetailsAPI"),


]