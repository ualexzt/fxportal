from django.urls import path
from .views import main_index, download_file

urlpatterns = [
    path('', main_index, name='index'),
    path('cmedata/<str:filename>', download_file)
]
