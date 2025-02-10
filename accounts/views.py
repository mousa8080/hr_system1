
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .form import signupForm

class singnUpview(CreateView):
  form_class=signupForm
  template_name = 'registration\signup.html'
  success_url = reverse_lazy('branches') 
