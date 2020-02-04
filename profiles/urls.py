from django.urls import path
from .views import profile_main, register, dashboard, subscription
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='profiles/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='profiles/logout.html'), name='logout'),
    path('password_reset/', PasswordResetView.as_view(template_name='profiles/password_reset.html'),
         name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='profiles/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>',
         PasswordResetConfirmView.as_view(template_name='profiles/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         PasswordResetCompleteView.as_view(template_name='profiles/password_reset_complete.html'),
         name='password_reset_complete'),
    path('', profile_main, name='profile_main'),
    path('dashboard/', dashboard, name='dashboard'),
    path('subscription/', subscription, name='subscription'),
]
