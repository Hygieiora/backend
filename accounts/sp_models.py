from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=(('M','Male'), ('F', 'Female')), default='M')
    
    class Meta:
        abstract = True