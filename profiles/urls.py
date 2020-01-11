from django.urls import path
from .views import profile, register, dashboard
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='profiles/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='profiles/logout.html'), name='logout'),
    path('', profile, name='profile_main'),
    path('dashboard/', dashboard, name='dashboard')
]