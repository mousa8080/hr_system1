from django import forms
from .models import Department
class newDepartmenttoBranche(forms.ModelForm):
    
      class Meta:
        model = Department
        fields = ["name",'phone']
