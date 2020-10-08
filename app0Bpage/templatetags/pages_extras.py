#recordar que files in emplatetagsfolder se leen en auto
#como si estubieran dentro del configsfile

from django import template
from app0Bpage.models import Page #Jala BESTPRACTICE
#from ..models import Page #ahora si funciona por ubicacion de dir
#//me marca no module named app0Bpage.templatetags.pages_extras.py

#usando template tags en vez de procesadores de contexto
#tranformamos una funcion en un tag simple
# y lo registramos en la libreria template

register = template.Library()
@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages
