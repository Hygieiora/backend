from django.test import TestCase
from accounts.models import Patient, Doctor, CustomUser


class TestModels(TestCase):
    def test_check_doctor_equals_doctor_profile(self):
        CustomUser.objects.create(
            password="testtest32",
            email="user@gmail.com",
            role="doctor",
            first_name="Dr",
        )
        doctor = CustomUser.objects.get(email="user@gmail.com")
        doctor_profile = Doctor.objects.get(user=doctor)
        self.assertEquals(doctor, doctor_profile.user)

    def test_check_patient_equals_patient_profile(self):
        CustomUser.objects.create(
            password="testtest32",
            email="user@st.knust.edu.gh",
            role="patient",
            first_name="User",
        )
        patient = CustomUser.objects.get(email="user@st.knust.edu.gh")
        patient_profile = Patient.objects.get(user=patient)
        self.assertEquals(patient, patient_profile.user)