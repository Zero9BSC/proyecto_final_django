from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_home, name='Home'),
    path('buscar_post', views.buscar_post, name='Buscar'),
    path('buscar/', views.buscar),
    path('crear_post/', views.crear_post, name='Crear'),
    path('mostrar_post/', views.mostrar_post, name='Mostrar'),
    path('mostrar_contacto/', views.mostrar_contacto, name='Contacto'),
    path('mostrar_about/', views.mostrar_about, name='About'),
    path('mostrar_noticias/', views.mostrar_noticias, name='Noticias'),
]