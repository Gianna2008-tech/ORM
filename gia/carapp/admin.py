from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'model', 'year']   # fields to show in admin list view
    search_fields = ['name', 'model']                # allow searching by name or model
    list_filter = ['year']                            # filters in admin sidebar

admin.site.register(Car, CarAdmin)

