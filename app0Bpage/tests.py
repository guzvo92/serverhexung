from django.test import TestCase

# Create your tests here.
Se utilizo concepto de las TEMPLATE TAGS
Renderiza las pagnas inferiores de contacto/about que son editables

*models.py [Page(RichTextField)(ordersort)]
//al tener el RichTextField en el sample.html existe link de editar
si usuario esta logueado
*admin.py [PageAdmin]

*apps.py [PagesConfig] (para cambiar config de verbose name)
*views.py [def page/ pasa por parametro la pagina a renderizar]
se utilizo el get_object_or_404 para cuando no haya objeto(pagina)
*urls.py ['<int:page_id>/']
*templates (sample.html)

en vez de utilizar procesadores de contexto
se utilizo el concepto de las template tags en [pages_extras.py]
contiene: @register.simple_tag(def get_page_list)
que es cargado en {template.Library()}
dif vs cntxproc :no tengo que configurar en settings.py

y al final en base.html se cargo como variable de esta manera:
{% load pages_extras %}
{% get_page_list as pagelist %}
{% for page in pagelist %}
