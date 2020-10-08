
from django.contrib import admin
from django.urls import path, include

from app0Bpage import views


urlpatterns = [

    path('<int:page_id>/',views.page, name="page"),


]
