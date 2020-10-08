from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Page(models.Model):
    #campo slug obliga a usar caract alfanumericos guiones y barras
    #los campos slug no nos permite usar caracteres especiales ni espacios
    title = models.CharField(verbose_name= "Titulo", max_length=200)
    content = RichTextField(verbose_name= "Contenido", max_length=200, null=True, blank=True)
    order = models.SmallIntegerField(verbose_name="Orden", default = 0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name= 'Pagina'
        verbose_name_plural = 'Paginas'
        ordering = ['order','title']

    def __str__(self):
        return self.title
