"""serverhexung URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from core import views
from appmain1admin import views

from pages.urls import pages_patterns


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.index, name="index"),
    path('admingen/', include('appmain1admin.urls')),
    path('watchlist/', include('appmain2watchlist.urls')),
    path('guildboard/', include('appmain3guildboard.urls')),
    path('mysteries/', include('appmain4mysteries.urls')),

    path('page/', include('app0Bpage.urls')),
    path('pages/', include(pages_patterns)), #ok
    path('services/', include('app0Bservices.urls')),  #ok
    path('blog/', include('app0Bblog.urls')),
    path('core/',include('core.urls')), #ok

]

#no adecuado para uso en produccion
from django.conf import settings

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
