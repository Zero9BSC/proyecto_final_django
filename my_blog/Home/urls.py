from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_home, name='Home'),
    path('buscar_post/', views.buscar_post, name='buscar_post'),
    path('buscar/', views.buscar, name='Buscar'),
    path('mostrar_post/', views.mostrar_post, name='Mostrar'),
    path('mostrar_contacto/', views.ContactCreateView.as_view(), name='Contacto'),
    path('mostrar_about/', views.mostrar_about, name='About'),
    path('mostrar_posteos/', views.mostrar_posteos, name='Mostrar Posteos'),
    path('eliminar_posteos/<post_id>', views.eliminar_posteos, name='Eliminar Posteos'),
    path('actualizar_posteos/<post_id>', views.actualizar_posteos, name='Actualizar Posteos'),
    path('signup/', views.create_user, name='Sign Up'),
    path('login/', views.AdminLoginView.as_view(), name='Login'),
    path('logout/', views.AdminLogoutView.as_view(), name='Logout'),
    path('editar_usuario/', views.editar_usuario, name='Editar Usuario'),
    path('perfil/<pk>', views.PerfilUpdateView.as_view(), name='Editar Perfil'),
    path('post_list/', views.PostList.as_view(), name='List'),
    path('post_detalle/<pk>', views.PostDetailView.as_view(), name='Detail'),
    path('post_confirm_delete/<pk>', views.PostDeleteView.as_view(), name='Delete'),
    path('post_edit/<pk>', views.PostUpdateView.as_view(), name='Update'),
    path('post_form/', views.PostCreateView.as_view(), name='Crear'),
    path('post_noticias/<categoria>', views.PostListNoticias.as_view(), name='Noticias'),
    path('post_reviews/<categoria>', views.PostListReviews.as_view(), name='Reviews'),
    path('post_gaming/<categoria>', views.PostListGaming.as_view(), name='Gaming'),
    path('post_software/<categoria>', views.PostListSoftware.as_view(), name='Software'),
    path('post_hardware/<categoria>', views.PostListHardware.as_view(), name='Hardware'),
]