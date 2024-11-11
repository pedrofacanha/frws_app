# data_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.worker_form, name='worker_form'),
]