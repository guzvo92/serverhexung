
from django.contrib import admin
from django.urls import path, include

from app0Bservices import views

urlpatterns = [

    path('',views.services, name="services"),
]
