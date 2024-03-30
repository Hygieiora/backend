from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Doctor, Patient, CustomUser

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'doctor':
            Doctor.objects.create(user=instance)
        elif instance.role == 'patient':
            Patient.objects.create(user=instance)

# @receiver(post_save, sender=CustomUser)
# def save_user_profile(sender, instance, **kwargs):
#     if instance.role == 'student':
#         instance.student_profile.save()
#     elif instance.role == 'doctor':
#         instance.doctor_profile.save()