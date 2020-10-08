from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def newhome(request): return render(request, "core/newhome.html")
def newsample(request): return render(request, "core/newsample.html")


def home(request): return render(request, "core/coffehome.html")
def store(request): return render(request, "core/coffestore.html")
def about(request): return render(request, "core/coffeabout.html")
def contact(request): return render(request, "core/coffecontact.html")
