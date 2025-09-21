# Ex02 Django ORM Web Application
# Date:21/09/2025
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books

# PROGRAM
''' 
admin.py

rom django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'department', 'position', 'salary', 'email', 'date_joined', 'is_active']
    search_fields = ['name', 'email']
    list_filter = ['department', 'position', 'is_active']

admin.site.register(Employee, EmployeeAdmin)

models.py

rom django.db import models
from django.utils.timezone import now   # Import now for default date

class Employee(models.Model):
    DEPARTMENTS = [
        ('HR', 'Human Resources'),
        ('IT', 'Information Technology'),
        ('FIN', 'Finance'),
        ('MKT', 'Marketing'),
    ]

    POSITIONS = [
        ('MN', 'Manager'),
        ('EX', 'Executive'),
        ('IN', 'Intern'),
    ]

    name = models.CharField(max_length=100)
    department = models.CharField(max_length=3, choices=DEPARTMENTS)
    position = models.CharField(max_length=2, choices=POSITIONS)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=50000.00)
    email = models.EmailField(unique=True, default='example@example.com')
    date_joined = models.DateField(default=now)  # Default current date
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    '''



# OUTPUT
![alt text](<Screenshot 2025-09-21 182719.png>)

# RESULT
Thus the program for creating a database using ORM hass been executed successfully
