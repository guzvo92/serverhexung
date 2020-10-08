

from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

    path('',views.guildboard, name="guildboard"),

    path('runrequest/',views.runrequest, name="runrequest"),
    path('runanalyzer/',views.runanalyzer, name="runanalyzer"),

]
