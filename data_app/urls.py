# data_app/urls.py
from django.urls import path
from . import views

# URL route for the Workers data
urlpatterns = [
    path('', views.worker_form, name='worker_form'),
]