
#[ URLS / Watchlist ]

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.watchlist, name="watchlist"),
    path('webkey/',views.webkey, name="webkeywatch"),
    path('clearallreg/',views.vista_clearallreg),

    



]
