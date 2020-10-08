#con esto podremos utilizar la variable context en cualquier template
#configurada en settings.py del proyecto/templates/options
from .models import Link

def contex_dict(request):
    context = {}
    links = Link.objects.all()
    for link in links:
        context[link.key] = link.url
    return context
