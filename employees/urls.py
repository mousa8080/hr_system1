from django.urls import path
from employees.ApIs import EmployeesCreateListView,postionApiView, EmployeesDetailsAPI
from . import views


urlpatterns = [

  path('emp/',EmployeesCreateListView.as_view(),name='emp'),
  path('emp/<int:pk>/',EmployeesDetailsAPI.as_view(),name='empdetails'),
  path('postion/',postionApiView.as_view(),name='postion'),


]