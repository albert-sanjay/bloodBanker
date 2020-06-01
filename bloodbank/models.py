from django.db import models
from phone_field import PhoneField
from accounts.models import Profile
from django.apps import apps
Profile = apps.get_model('accounts','Profile')

# Create your models here.
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
    phone = PhoneField(help_text='Contact Number')


class Inventory(models.Model):
    blood_bag_id = models.CharField(max_length=20)
    blood_type = models.CharField(max_length=3)
    type_rh = models.CharField(max_length=20)
    blood_volume = models.PositiveIntegerField()
    recieve_date = models.DateField(auto_now=False, auto_now_add=False)
    expire_date = models.DateField(auto_now=False, auto_now_add=False)
    blood_status = models.CharField(max_length=20)
    blood_donation = models.ForeignKey('BloodDonation', on_delete=models.CASCADE)
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE)



class BloodDonation(models.Model):
    blood_qty = models.PositiveIntegerField()
    blood_type = models.CharField(max_length=3)
    type_rh = models.CharField(max_length=20)
    donate_date = models.DateField(auto_now=False, auto_now_add=False)
    result_date = models.DateField(auto_now=False, auto_now_add=False)
    blood_status = models.CharField(max_length=20)
    donor = models.ForeignKey('Donor', on_delete=models.CASCADE)


class Request(models.Model):
    blood_type = models.CharField(max_length=10, choices=BLOOD_TYPES)
    type_rh = models.CharField(max_length=20)
    request_date = models.DateField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)


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
    phone = PhoneField(help_text='Contact Number')
    blood_type = models.CharField(max_length=10, choices=BLOOD_TYPES)
    type_rh = models.CharField(max_length=20)
    user = models.ForeignKey('Profile',on_delete=models.CASCADE)
