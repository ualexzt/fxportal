from django.urls import path
from .views import profile_main, register, dashboard, traiders_diary
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='profiles/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='profiles/logout.html'), name='logout'),
    path('', profile_main, name='profile_main'),
    path('dashboard/', dashboard, name='dashboard'),
    path('traidiary/', traiders_diary, name='traiders_diary')
]