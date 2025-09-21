from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'department', 'position', 'salary', 'email', 'date_joined', 'is_active']
    search_fields = ['name', 'email']
    list_filter = ['department', 'position', 'is_active']

admin.site.register(Employee, EmployeeAdmin)
