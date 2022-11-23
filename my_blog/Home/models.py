from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=90)
    sub_titulo = models.CharField(max_length=90)
    fecha = models.DateField()
    categoria = models.CharField(max_length=20, default='Uncategorize')
    texto = models.CharField(max_length=254)

    def __str__(self):
        return f'Titulo: {self.titulo}, Sub Titulo: {self.sub_titulo}, Fecha: {self.fecha}, Categoria: {self.categoria},Contenido: {self.texto}' #Categoria: {self.categoria},

class PostNoticias(models.Model):
    titulo = models.CharField(max_length=90)
    sub_titulo = models.CharField(max_length=90)
    fecha = models.DateField()
    texto = models.CharField(max_length=254)

class PostReviews(models.Model):
    titulo = models.CharField(max_length=90)
    sub_titulo = models.CharField(max_length=90)
    fecha = models.DateField()
    texto = models.CharField(max_length=254)

class PostGaming(models.Model):
    titulo = models.CharField(max_length=90)
    sub_titulo = models.CharField(max_length=90)
    fecha = models.DateField()
    texto = models.CharField(max_length=254)

class PostSoftware(models.Model):
    titulo = models.CharField(max_length=90)
    sub_titulo = models.CharField(max_length=90)
    fecha = models.DateField()
    texto = models.CharField(max_length=254)

class PostHardware(models.Model):
    titulo = models.CharField(max_length=90)
    sub_titulo = models.CharField(max_length=90)
    fecha = models.DateField()
    texto = models.CharField(max_length=254)

class Contacto(models.Model):
    nombre = models.CharField(max_length=90)
    email = models.EmailField()
    consulta = models.CharField(max_length=254)