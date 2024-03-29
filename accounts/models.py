from django.db import models
from sp_models import BaseModel

# Create your models here.
class Patient(BaseModel):
    school_email = models.CharField(max_length=256)
    student_id = models.IntegerField(max_length=8)
    programme = models.CharField(max_length=256)
    year_of_study = models.IntegerField(max_length=1)

    def __str__(self):
        return f"{self.user.email} | {self.user.first_name} - {self.student_id}"


class Doctor(BaseModel):
    specialty = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.user.email} | {self.specialty}"
