# general_info/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('people/', views.person_list, name='workers_list'),
]