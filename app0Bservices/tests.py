[app0Bservices]
Renderiza los servicios en la pagina servicios

*models.py [Service]
*admin.py [ServiceAdmin]
*apps.py [ServicesConfig] (para cambiar config de verbose name)
*views.py [def services/ solo pasa los servicios de contexto a un render]
*urls.py
*templates (services.html)

PIPELINES HOOKS
*server/settings.py/INSTALLEDAPPS ---- 'app0Bservices.apps.App0BservicesConfig'
*server/urls.py/URLPATTERNS ---- path('services/', include('app0Bservices.urls'))
