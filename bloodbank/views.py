from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Request(TemplateView):
    template_name = "bloodbank/request.html"
