from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from django.dispatch import receiver

CATEGORIES_CHOICES = (
    ("", "Select Option"),
    ("Noticias", "Noticias"),
    ("Reviews", "Reviews"),
    ("Gaming", "Gaming"),
    ("Sofrware", "Sofrware"),
    ("Hardware", "Hardware"),
)



class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombres = models.CharField('Nombres de Autor',max_length = 255, null = False, blank = False)
    apellidos = models.CharField('Apellidos de autor', max_length = 255, null = False, blank = False)
    facebook = models.URLField('Facebook', null = True, blank = True)
    twitter = models.URLField('Twitter', null = True, blank = True)
    instagram = models.URLField('Instagram', null = True, blank = True)
    web = models.URLField('Web', null = True, blank = True)
    correo = models.EmailField('Correo Electrónico', blank = False, null = False)
    estado = models.BooleanField('Autor Activo/No Activo',default = True)
    fecha_creacion = models.DateField('Fecha de Creación', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return "{0},{1}".format(self.apellidos, self.nombres)

class Perfil(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    correo = models.EmailField(blank = False, null = False)
    imagen = models.ImageField(upload_to='avatar/', null=True, blank=True)
    nombre = models.CharField(max_length = 255, null = False, blank = False)
    apellido = models.CharField(max_length = 255, null = False, blank = False)
    facebook = models.URLField(null = True, blank = True)
    twitter = models.URLField(null = True, blank = True)
    instagram = models.URLField(null = True, blank = True)
    web = models.URLField(null = True, blank = True)

    USERNAME_FIELD = 'usuario'

    def __str__(self):  
        return self.usuario.username




class Post(models.Model):
    titulo = models.CharField(max_length=90)
    imagen = models.ImageField(null= True, blank=True, upload_to='images/')
    sub_titulo = models.CharField(max_length=90)
    autor = models.ForeignKey(Perfil, on_delete = models.CASCADE)
    fecha = models.DateField()
    categoria = models.CharField(max_length=20, choices = CATEGORIES_CHOICES, blank= False, default=1)
    texto = RichTextField()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'Titulo: {self.titulo}, Fecha: {self.fecha}, Categoria: {self.categoria}'


class Contacto(models.Model):
    nombre = models.CharField(max_length=90)
    email = models.EmailField()
    consulta = models.CharField(max_length=254)

    def __str__(self):
        return f'Nombre: {self.nombre}, Email: {self.email}, Consulta: {self.consulta}'



