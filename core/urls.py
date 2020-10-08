
#[URLS CORE]

from django.contrib import admin
from django.urls import path

from core import views


urlpatterns = [

    path('', views.newhome, name="newhome"),
    path('newsample', views.newsample, name="newsample"),

    path('coffehome', views.home, name="coffehome"),
    path('coffestore/',views.store, name="coffestore"),
    path('coffeabout/',views.about, name="coffeabout"),
    path('coffecontact/',views.contact, name="coffecontact"),


]
