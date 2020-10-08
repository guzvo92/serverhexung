
from django.contrib import admin
from django.urls import path, include

from app0Bblog import views

urlpatterns = [

    path('',views.blog, name="blog"),
    #parametros dinamicos se pasan siempre como un string

    #-----path('category/<category_id>/', views.category, name)
    #por eso mejor lo tranformo en entero

    path('category/<int:category_id>/', views.category, name= 'category'),



]
