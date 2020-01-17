from django.urls import path
from .views import main_index

urlpatterns = [
    path('', main_index, name='index'),
]
