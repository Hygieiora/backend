from django.contrib import admin
from .models import Doctor, Patient, CustomUser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Doctor)
admin.site.register(Patient)
