from django.test import TestCase


Renderiza los post o entradas con su autor correspondente
aunque para crearlas solo es desde el panel de admnistrador

*models.py [CategoryAdmin]
//al tener el RichTextField en el sample.html existe link de editar
si usuario esta logueado
*admin.py [CategoryAdmin][PostAdmin]

*apps.py [PagesConfig] (para cambiar config de verbose name)
*views.py [def page/ pasa por parametro la pagina a renderizar]
se utilizo el get_object_or_404 para cuando no haya objeto(pagina)
*urls.py ['<int:page_id>/']
*templates (sample.html)

en vez de utilizar procesadores de contexto
se utilizo el concepto de las template tags dentro de
[pages_extras.py] trae: @register.simple_tag(def get_page_list)
que es cargado en {template.Library()} sin tener que configurar
los settings.py del proyecto como con los context processor

y al final en base.html se cargo como variable de esta manera:
{% load pages_extras %}
{% get_page_list as pagelist %}
{% for page in pagelist %}
