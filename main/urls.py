from django.urls import path
from .views import main_index, download_file, contact

urlpatterns = [
    path('', main_index, name='index'),
    path('contact/', contact, name='contacts'),
    path('cmedata/<str:filename>', download_file),
]
