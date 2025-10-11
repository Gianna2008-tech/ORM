# Ex02 Django ORM Web Application
# Date:
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# ENTITY RELATIONSHIP DIAGRAM
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
```
admin.py

from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'model', 'year']   
    search_fields = ['name', 'model']                
    list_filter = ['year']                          

admin.site.register(Car, CarAdmin)


models.py

from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f"{self.name} {self.model}"
```
# OUTPUT
Include the screenshot of your admin page.

<img width="1895" height="913" alt="car github" src="https://github.com/user-attachments/assets/5a8b046d-58cf-4e4c-98b2-20d22ea7ba4a" />

# RESULT
Thus the program for creating a database using ORM hass been executed successfully
