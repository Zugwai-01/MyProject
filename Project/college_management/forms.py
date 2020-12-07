from django import forms
from .models import Student,Department

class FormName(forms.ModelForm):
    class Meta:
        model = Student
        fields ='__all__'

class DeptForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
