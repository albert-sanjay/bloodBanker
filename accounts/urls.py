from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import SignUpView, ActivateAccount

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    # LOGIN & LOGOUT
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
