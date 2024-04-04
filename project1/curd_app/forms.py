from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

        widgets = {
            "employee_id": forms.NumberInput(),
            "employee_name": forms.TextInput(attrs={"class": "form-control"}),
            "employee_location_mode": forms.Select(attrs={"class": "form-control"}),
            "employee_salary_mode": forms.Select(attrs={"class": "form-control"}),
            "working_time": forms.NumberInput()
        }