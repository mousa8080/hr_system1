from django.shortcuts import render
# from django.http import HttpResponse
from .models import Branches,Department
from .forms import newDepartmenttoBranche
from django.views.generic import ListView

# # Create your views here.
# def branches(request):
#   b=Branches.objects.all()
  
#   # str="<ul>"
#   # for branches in b:
#   #   str+="<li>"+Branches.name+"</li>"
#   # str+="</ul>"
#   # return HttpResponse(str)
#   # return render(request,'branches.html',{'branches':b})
#   # pass
# def newDepartmenttoBranche(requst,branches_id):
#   form=newDepartmenttoBranche()
#   # if Department.objects.filter(name=celaned_data['name']):
#   return render(requst,'company','newDepartmenttoBranche.html')
class branchesView(ListView):
  model=Branches
  template_name='company/branches.html'
