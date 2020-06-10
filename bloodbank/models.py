from django.db import models
import datetime
from phone_field import PhoneField
from django.utils import timezone
from faker import Faker
from django.conf import settings
# from accounts.models import Profile
# from django.apps import apps
# Profile = apps.get_model('accounts','Profile', require_ready=True)

# Create your models here.
fake = Faker()

BLOOD_TYPES = [
    ('A','A'),
    ('B','B'),
    ('AB','AB'),
    ('O','O'),
]

class Hospital(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    blood_bag_id = models.CharField(max_length=20, default=fake.ssn())
    blood_type = models.CharField(max_length=3)
    type_rh = models.CharField(max_length=20)
    blood_volume = models.PositiveIntegerField()
    recieve_date = models.DateField(auto_now=False, auto_now_add=False)
    expire_date = models.DateField(auto_now=False, auto_now_add=False)
    blood_status = models.CharField(max_length=20)
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE)

    def __str__(self):
        return self.blood_type



class BloodDonation(models.Model):
    blood_qty = models.PositiveIntegerField()
    blood_type = models.CharField(max_length=3)
    type_rh = models.CharField(max_length=20)
    donate_date = models.DateField(auto_now=False, auto_now_add=False)
    result_date = models.DateField(auto_now=False, auto_now_add=False)
    blood_status = models.CharField(max_length=20)
    donor = models.ForeignKey('Donor', on_delete=models.CASCADE)

    def __str__(self):
        return self.blood_type


GENDER_CHOICES = [
    ('Male','Male'),
    ('Female','Female'),
]

class Donor(models.Model):
    name = models.CharField(max_length=256)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=256)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=10)
    blood_type = models.CharField(max_length=10, choices=BLOOD_TYPES)
    type_rh = models.CharField(max_length=20)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


class Request(models.Model):
    blood_type = models.CharField(max_length=10, choices=BLOOD_TYPES)
    type_rh = models.CharField(max_length=20)
    request_date = models.DateField(default=timezone.now)
    request_status = models.CharField(max_length=20)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)


    def __str__(self):
        return self.blood_type
