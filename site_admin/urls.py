from django.urls import path
from django.contrib.auth import views as auth_views
from .views import DashboardPage, AdminLoginView, DonorListView, InventoryListView, RequestListView
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect

app_name = 'site_admin'

urlpatterns = [
    path('', DashboardPage.as_view(), name='dashboard'),
    path('donor_detail/', DonorListView.as_view(), name='donor_detail'),
    path('blood_stock/', InventoryListView.as_view(), name='inventory'),
    path('view_requests/', RequestListView.as_view(), name='request'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True,template_name='site_admin/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='accounts:login'), name='logout'),
]
