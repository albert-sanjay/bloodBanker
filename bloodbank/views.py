from django.shortcuts import render
from django.views.generic import TemplateView,CreateView, DetailView
from bloodbank.models import Donor, Request
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class CreateRequestView(CreateView):
    fields = ('blood_type', 'type_rh', 'request_date')
    model = Request

    # def get_form(self):
    #     '''add date picker in forms'''
    #     from django.forms import SelectDateWidget
    #     form = super(CreateRequestView, self).get_form()
    #     form.fields['request_date'].widget = SelectDateWidget()
    #     return form


# NOTE: class CreateDonorView(CreateView):
            # fields = ('name', ...)
            # model = models.Donor
# NOTE: template_name = model_form.html

class CreateDonorView(LoginRequiredMixin, CreateView):
    fields = ('name', 'gender', 'age',
               'address', 'email', 'phone', 'blood_type', 'type_rh'
               )
    model = Donor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        donor = Donor.objects.all()
        context["donor"] = donor
        return context


class DonorDetailView(DetailView):
    model = Donor
    template_name = 'bloodbank/donor_detail.html'
