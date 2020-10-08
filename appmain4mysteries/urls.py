
#[URLS/ Mysteries]
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.mysteries, name='mysteries'),
    path('clear/<int:id>',views.clear, name='clear'),
    path('save_mystery/', views.save_mystery, name='savemystery'),

    #path mysteries es por el render que tengo en el menu nav
]
