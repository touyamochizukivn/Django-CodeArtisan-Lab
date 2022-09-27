from django.forms import ModelForm

from . import models


class EmployeeForm(ModelForm):
    class Meta:
        model = models.Employee
        fields = ('name', 'email', 'address', )


class StudentForm(ModelForm):
    class Meta:
        model = models.Student
        fields = '__all__'


