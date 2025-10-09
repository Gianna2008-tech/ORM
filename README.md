# Ex02 Django ORM Web Application
# Date:22/09/2025
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

    def __str__(self):
        return f"{self.name} {self.model}"


    ```


# OUTPUT 
<img width="1905" height="1079" alt="Screenshot 2025-09-29 212046" src="https://github.com/user-attachments/assets/a56d2dc0-cb12-41cb-9ecf-d3d099e4d34b" />



# RESULT
Thus the program for creating a database using ORM hass been executed successfully
