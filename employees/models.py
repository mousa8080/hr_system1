from django.db import models

# Create your models here.

class Employees(models.Model):
  name=models.CharField(max_length=50,)
  age=models.IntegerField()
  salary=models.IntegerField()
  def __str__(self):
    return self.name


class postion(models.Model):
  name=models.CharField(max_length=50,)
  yeencears_of_exper=models.IntegerField()
  discription=models.CharField(max_length=100)
  postion_key=models.ForeignKey(Employees,related_name='postion_employees',on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name