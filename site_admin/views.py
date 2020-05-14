from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, HttpResponseRedirect

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
