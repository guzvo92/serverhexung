#from django.shortcuts import render, get_object_or_404, get_list_or_404 ya nolo uso
#indispensable para las VBC
from django.views.generic.list import ListView #importa una lista
from django.views.generic.detail import DetailView #importa 1 solo objeto
from django.views.generic.edit import CreateView #importa 1 solo objeto
from django.urls import reverse #para hacer redireccion

from .models import Page
'''
#vista de las instancias de un modelo
def pages(request):
    pages = get_list_or_404(Page)
    return render(request, 'pages/pages.html', {'pages':pages})

#vista para una unica instancia de un modelo
def page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/page.html', {'page':page})
'''

class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page


class PageCreate(CreateView):
    model = Page
    fields = ['title','content','order']
    #success_url = reverse('pages:pages') asi no jala

    #metodo de las vistas basadas en clases
    def get_success_url(self):
        return reverse('pages:pages')
