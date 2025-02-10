from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class signupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    usable_passward=None
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
