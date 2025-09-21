from django.db import models
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

