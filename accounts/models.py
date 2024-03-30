from django.contrib.auth.models import AbstractUser
from django.db import models
from .sp_models import BaseModel

# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    )
    role = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)


class Patient(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='patient')
    school_email = models.CharField(max_length=256)
    student_id = models.IntegerField(blank=True, null=True)
    programme = models.CharField(max_length=256)
    year_of_study = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.email} | {self.user.first_name} - {self.student_id}"


class Doctor(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='doctor')
    specialty = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.user.email} | {self.specialty}"
