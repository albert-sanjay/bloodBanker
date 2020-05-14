from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = "index.html"

class ContactPage(TemplateView):
    template_name = "contact.html"

class FaqsPage(TemplateView):
    template_name = "faqs.html"
