from django.db import models
# Create your models here.
class Branches(models.Model):
  name=models.CharField(max_length=50)
  discription=models.CharField(max_length=50)
  def __str__(self):
    return self.name

class Department(models.Model):
  name=models.CharField(max_length=50)
  phone=models.CharField(max_length=50)
  email=models.CharField(max_length=50)
  Branches=models.ForeignKey(Branches,related_name="Branches",on_delete=models.CASCADE)
  class meta:
    unique_together=('name','Branches')
  def __str__(self):
    return self.name
