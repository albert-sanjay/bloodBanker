from django.urls import path
from bloodbank.views import CreateRequestView, CreateDonorView

app_name = 'bloodbank'

urlpatterns = [
    path('request/', CreateRequestView.as_view(), name='request'),
    path('donate/', CreateDonorView.as_view(), name='donate')
]
