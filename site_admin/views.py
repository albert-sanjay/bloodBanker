from django.shortcuts import render
from django.views.generic import TemplateView, View, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.apps import apps
Donor = apps.get_model('bloodbank', 'Donor')
Inventory = apps.get_model('bloodbank', 'Inventory')
Request = apps.get_model('bloodbank', 'Request')

# Create your views here.
class TestUserIsSuperuser(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class DashboardPage(LoginRequiredMixin,TestUserIsSuperuser,TemplateView):
    template_name = 'site_admin/base.html'


class AdminLoginView(View):
    template_name = 'site_admin/login.html'
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user.is_superuser:
            login(request, user)
            return HttpResponseRedirect('site_admin:dashboard')

        else:
            return HttpResponse('Not superuser')

        return render(request, 'site_admin/login.html')



class DonorListView(ListView):
    context_object_name = 'donor'
    model = Donor
    template_name = 'site_admin/donor_detail.html'


class InventoryListView(ListView):
    context_object_name = 'inventory'
    model = Inventory
    template_name = 'site_admin/inventory_list.html'


class RequestListView(ListView):
    context_object_name = 'request'
    model = Request
    template_name = 'site_admin/request_list.html'
