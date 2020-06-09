from django.contrib import admin
from bloodbank.models import Inventory, Hospital, Donor, Request, BloodDonation

# Register your models here.
admin.site.register(Inventory)
admin.site.register(Hospital)
admin.site.register(Donor)
admin.site.register(BloodDonation)
admin.site.register(Request)
