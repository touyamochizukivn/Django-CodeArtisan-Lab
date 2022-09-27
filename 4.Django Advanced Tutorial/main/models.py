from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True)
    address = models.TextField(max_length=500, null=True)


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=100)
    address = models.TextField(max_length=500)