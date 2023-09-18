from django.contrib import admin

# Register your models here.
from .models import Organization, Office, Employee

admin.site.register(Organization)
admin.site.register(Office)
admin.site.register(Employee)
