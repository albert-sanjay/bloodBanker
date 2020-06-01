from django.urls import path
from bloodbank.views import Request

app_name = 'bloodbank'

urlpatterns = [
    path('request/', Request.as_view(), name='request')
]
