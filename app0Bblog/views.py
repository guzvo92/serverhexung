from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.

def blog(request):
    posts = Post.objects.all()
    return render(request, "blog.html",
                    {'posts':posts})

def category(request, category_id):
    #.get recoger 1 unico registro filtrando por campos (id)

    #-----category = Category.objects.get(id=category_id)
    #tengo actualmente 3 categorias si renderizo http://localhost:8000/blog/category/3/
    #funciona pero si lo hago con 4 me manda un error
    #el 1,2,3,4 es el identificador
    #lo solucionaremos con el accesor get_object_or_404

    category = get_object_or_404(Category,id=category_id)
    return render (request, "category.html",{'category':category})
