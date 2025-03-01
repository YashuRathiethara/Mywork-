from django import forms
from employee.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'  # Correct usage as a string but without extra characters
