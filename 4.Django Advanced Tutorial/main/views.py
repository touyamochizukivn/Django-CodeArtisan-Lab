from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from . import forms


def home(request):
    form = forms.EmployeeForm
    if request.method == 'POST':
        form = forms.EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data has been added')
            return redirect('/')
    return render(request, 'home.html', {'form': form, })


def student(request):
    form = forms.StudentForm
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data has been added')
            return redirect('/student')
    return render(request, 'student.html', {'form': form, })


def register(request):
    form = UserCreationForm
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User has been registered')
    return render(request, 'registration/register.html', {'form': form, })