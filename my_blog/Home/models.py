from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

CATEGORIES_CHOICES = (
    ("", "Select Option"),
    ("Noticias", "Noticias"),
    ("Reviews", "Reviews"),
    ("Gaming", "Gaming"),
    ("Sofrware", "Sofrware"),
    ("Hardware", "Hardware"),
)


class Post(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=90)
    imagen = models.ImageField(null= True, blank=True, upload_to='images/')
    sub_titulo = models.CharField(max_length=90)
    fecha = models.DateField()
    categoria = models.CharField(max_length=20, choices = CATEGORIES_CHOICES, blank= False, default=1)
    texto = RichTextField()

    def __str__(self):
        return f'Titulo: {self.titulo}, Imagen: {self.imagen}, Sub Titulo: {self.sub_titulo}, Fecha: {self.fecha}, Categoria: {self.categoria},Contenido: {self.texto}'

#User: {self.user},
class Contacto(models.Model):
    nombre = models.CharField(max_length=90)
    email = models.EmailField()
    consulta = models.CharField(max_length=254)


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='images/', null=True, blank=True)