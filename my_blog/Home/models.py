from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=90)
    sub_titulo = models.CharField(max_length=90)
    fecha = models.DateField()
    texto = models.CharField(max_length=254)

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