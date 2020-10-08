
#[ URLS / admin ]

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [

    path('', views.admingen, name="admingen"),
    path('save_charinmatrix/', views.save_metcharinmatrix, name='savecharinmatrix'),
    path('clearchar/<int:id>',views.clearchar, name='clearchar'),
]
