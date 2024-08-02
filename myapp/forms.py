from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'nameid', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'emailid', 'placeholder': 'Enter your email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'passwordid', 'placeholder': 'Enter your password'}),
        }
        error_messages = {
            'name': {
                'required': 'Please enter name.',
            },
            'email': {
                'required': 'Please enter email.',
            },
            'password': {
                'required': 'Please enter password.',
            }
        }
