from django.contrib import admin
from .models import Category, Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields= ('created','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields= ('created','updated')

    #Post categories PORQUE CATEGORIES__NAME no funciono
    list_display =('title','author','published','post_categories')
    #ordenando por autor y luego por fecha de pub
    ordering = ('author','published')
    #ordering = ('author',)
    #tiene que ir con una coma para que identifique una tupla
    #y no marque errores

    #search_fields= ('title',)
    #search_fields= ('title','content')
    #aparece un buscador que busca por Titulo

    #para modelos relacionados con otra estructura
    #porque no es un campo que pueda ser mostrado
    #como una sola columna
    search_fields = ('author__username',)

    #jerarquia por fechas
    date_hierarchy = 'published'

    #FILTRADO por nombre y categoria
    list_filter = ('author__username', 'categories__name')

    def post_categories(self,obj):
        return ", " .join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorias"

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post, PostAdmin)
