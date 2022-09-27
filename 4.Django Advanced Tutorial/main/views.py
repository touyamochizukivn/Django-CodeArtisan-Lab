from django.shortcuts import render, redirect
from django.contrib import messages

from . import forms


def home(request):
    form = forms.EmployeeForm
    if request.method == 'POST':
        empForm = forms.EmployeeForm(request.POST)
        if empForm.is_valid():
            empForm.save()
            messages.success(request, 'Data has been added')
            return redirect('/')
    return render(request, 'home.html', {'form': form,})


def student(request):
    form = forms.StudentForm
    if request.method == 'POST':
        stuForm = forms.StudentForm(request.POST)
        if stuForm.is_valid():
            stuForm.save()
            messages.success(request, 'Data has been added')
            return redirect('/student')
    return render(request, 'student.html', {'form': form})