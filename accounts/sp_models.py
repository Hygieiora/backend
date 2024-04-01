from django.db import models

class BaseModel(models.Model):
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=(('M','Male'), ('F', 'Female')))
    
    class Meta:
        abstract = True