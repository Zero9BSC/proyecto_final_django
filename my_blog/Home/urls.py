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
    path('mostrar_posteos/', views.mostrar_posteos, name='Mostrar Posteos'),
    path('eliminar_posteos/<post_id>', views.eliminar_posteos, name='Eliminar Posteos'),
    path('actualizar_posteos/<post_id>', views.actualizar_posteos, name='Actualizar Posteos'),
    #path('signup/', views.SignUpView.as_view(), name='Sign Up'),
    path('post_list/', views.PostList.as_view(), name='List'),
    path('post_detalle/<pk>', views.PostDetailView.as_view(), name='Detail'),
    path('post_confirm_delete/<pk>', views.PostDeleteView.as_view(), name='Delete'),
    path('post_edit/<pk>', views.PostUpdateView.as_view(), name='Update'),
    path('post_form/', views.PostCreateView.as_view(), name='Create'),
]