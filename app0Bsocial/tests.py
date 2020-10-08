from django.test import TestCase

#settings.py/INSTALLEDAPPS----------------------------
#'app0Bsocial.apps.App0BsocialConfig'

#settings.py/TEMPLATES--------------------------------------
#'app0Bsocial.processors.contex_dict'


#-----------------------------------------------------------
'''
Aqui se reviso el concepto de los context processors

Ataca los iconos de las redes sociales en la parte inferior del base .html
*admin.py (LinkAdmin)
*models.py (Link/slug+urlfields)
*apps.py (para cambiar config de verbose name)

*processors.py
(funcion contex_dict que a la clave primaria le asigna la url configurada)

esa funcion debera ser cargada en settings.py del proyecto
en la seccion de contextprocessors 'social.processors.contex_dict'
'''
