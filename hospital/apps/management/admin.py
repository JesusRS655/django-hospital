from django.contrib import admin
from .models import Doctor, Patient, Department, Director

# Register your models here.

admin.site.register(Director)
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Patient)
