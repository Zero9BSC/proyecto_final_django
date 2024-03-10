from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required # DECORATORS para vistas basadas en Funciones
from django.contrib.auth.mixins import LoginRequiredMixin # MIXINS para vistas basadas en Clases

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# from django.db.models.signals import post_delete
# from django.dispatch import receiver

from .models import *
from .forms import *


# VISTAS BASADAS EN FUNCIONES
def mostrar_home(request):
    latest_posts = Post.objects.order_by('-fecha')[:5]
    perfil_usuario = None
    if request.user.is_authenticated:
        perfil_usuario = Perfil.objects.get(usuario=request.user)
    return render(request, 'index.html', {'latest_posts': latest_posts, 'perfil_usuario': perfil_usuario})

def buscar_post(request):
    
    return render(request, "buscar_post.html")

def buscar(request):
    titulo = request.GET.get('titulo')

    if titulo:  
        posts = Post.objects.filter(titulo__icontains=titulo)
        if posts:
            return render(request, "buscar_post.html", {"post": posts, "titulo": titulo})
        else:
            respuesta = "No se encontraron resultados para la búsqueda."
            return render(request, "buscar_post.html", {"respuesta": respuesta})
    elif request.method == 'GET' and not titulo:
        mensaje = "Debe ingresar un parámetro para buscar."
        return render(request, "buscar_post.html", {"mensaje": mensaje})
    else:
        return render(request, "buscar_post.html")


def mostrar_post(request):
    return render(request, "post.html") #Solo como ejemplo para mostrar como se ve la template "post.html"

def mostrar_contacto(request):
    return render(request, "contacto.html")
    
def mostrar_about(request):
    return render(request, "about.html")

def crear_consulta(request):
    if request.method == "POST":
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('Home')
    else:
        formulario = ContactoForm()
    return render(request, "contacto.html", {"formulario": formulario})

def mostrar_posteos(request):
    posteos = Post.objects.all()
    context = {'posteos': posteos}
    
    # Determinar si el usuario logueado es el autor de cada post (si está logueado)
    if request.user.is_authenticated:
        for post in posteos:
            post.es_autor = post.autor.usuario == request.user
    else:
        # Si no está logueado, establecer es_autor como False para todos los posteos
        for post in posteos:
            post.es_autor = False

    return render(request, 'mostrar_posteos.html', context=context)


@login_required
def eliminar_posteos(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    # Verificar si el usuario actual es el autor del post
    if post.autor.usuario == request.user:
        # Obtener la imagen asociada al post y eliminarla si existe
        if post.imagen:
            post.imagen.delete()
        
        # Eliminar el post
        post.delete()
        
    return redirect('Mostrar Posteos')


@login_required
def actualizar_posteos(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # Verifica si el usuario actual es el autor del post
    if post.autor.usuario == request.user:
        if request.method == "POST":
            formulario = CrearPostForm(request.POST, request.FILES, instance=post)
            if formulario.is_valid():
                # Eliminar la imagen anterior si se proporciona una nueva
                if 'nueva_imagen' in request.FILES:
                    if post.imagen:
                        default_storage.delete(post.imagen.path)
                    post.imagen = request.FILES['nueva_imagen']
                formulario.save()
                return redirect('Mostrar Posteos')
        else:
            formulario = CrearPostForm(instance=post)
        categorias_disponibles = ['Noticias', 'Reviews', 'Gaming', 'Software', 'Hardware']  # Agregar categorías disponibles
        return render(request, "actualizar_post.html", {"formulario": formulario, "categorias": categorias_disponibles})
    else:
        return HttpResponse("No tienes permiso para realizar esta acción.")


@login_required
def editar_usuario(request):
    perfil = Perfil.objects.get(usuario=request.user)

    if request.method == 'POST':
        usuario_form = UserEditForm(request.POST, instance=request.user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil)

        if usuario_form.is_valid() and perfil_form.is_valid():
            usuario_form.save()
            perfil_form.save()
            return redirect('Home')
    else:
        usuario_form = UserEditForm(instance=request.user)
        perfil_form = PerfilForm(instance=perfil)

    # Obtener la URL de la imagen redondeada de tamaño pequeño si existe
    imagen_pequena_url = perfil.imagen.url if perfil.imagen else None

    return render(request, 'admin_update.html', {
        'form': usuario_form,
        'form2': perfil_form,
        'usuario': request.user,
        'imagen_pequena_url': imagen_pequena_url,  # Pasar la URL de la imagen al template
    })

def create_user(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        perfil_form = PerfilForm(request.POST, request.FILES)
        if user_form.is_valid() and perfil_form.is_valid():
            user = user_form.save()
            
            perfil = perfil_form.save(commit=False)
            perfil.usuario = user  # Asigna el usuario recién creado al perfil
            
            # Si hay una imagen cargada, guárdala en el perfil
            if 'imagen' in request.FILES:
                perfil.imagen = request.FILES['imagen']
            
            perfil.save()

            return redirect('Home')  # Redirige a la página de inicio
    else:
        user_form = UserCreationForm()
        perfil_form = PerfilForm()
    return render(request, 'registro.html', {
        'user_form': user_form, 
        'perfil_form': perfil_form
    })



# VISTAS BASADAS EN CLASES
class PostDetailView(DetailView):

    model = Post
    template_name = 'Home/post_detalle.html'


class PostList(ListView):

    model = Post
    template_name = 'Home/post_list.html'

class PostDeleteView(LoginRequiredMixin, DeleteView):

    model = Post
    success_url = '/post_list'

class PostUpdateView(LoginRequiredMixin, UpdateView):

    model = Post
    success_url = '/post_list'
    fields = ['titulo', 'imagen', 'sub_titulo', 'categoria', 'fecha', 'texto']


class PostCreateView(LoginRequiredMixin, CreateView):

    model = Post
    success_url = '/post_list'
    fields = ['titulo', 'sub_titulo', 'imagen', 'fecha', 'categoria', 'texto']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.autor = Perfil.objects.get(usuario=self.request.user.id)
        post.save()
        return HttpResponseRedirect('/post_list')

class ContactCreateView(CreateView):
    model = Contacto
    form_class = ContactoForm
    template_name = 'contacto.html'
    success_url = reverse_lazy('Home')


# CATEGORIAS
class PostListNoticias(ListView):
    model = Post
    template_name = 'post_noticias.html'

    def get_queryset(self):
        queryset = Post.objects.filter(categoria__icontains = self.kwargs['categoria'])

        return queryset

class PostListReviews(ListView):
    model = Post
    template_name = 'post_reviews.html'

    def get_queryset(self):
        queryset = Post.objects.filter(categoria__icontains = self.kwargs['categoria'])

        return queryset

class PostListGaming(ListView):
    model = Post
    template_name = 'post_gaming.html'

    def get_queryset(self):
        queryset = Post.objects.filter(categoria__icontains = self.kwargs['categoria'])

        return queryset

class PostListSoftware(ListView):
    model = Post
    template_name = 'post_software.html'

    def get_queryset(self):
        queryset = Post.objects.filter(categoria__icontains = self.kwargs['categoria'])

        return queryset

class PostListHardware(ListView):
    model = Post
    template_name = 'post_hardware.html'

    def get_queryset(self):
        queryset = Post.objects.filter(categoria__icontains = self.kwargs['categoria'])

        return queryset


#SIGNUP, LOGIN Y LOGOUT
class SignUpView(CreateView):

    model = Perfil
    form_class = SignUpForm
    success_url = reverse_lazy('Home')
    template_name = 'perfil_form.html'

    def form_valid(self, form):

        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('index.html')

class AdminLoginView(LoginView):
    template_name = 'login.html'

class AdminLogoutView(LogoutView):
    success_url = reverse_lazy('Home')

class PerfilUpdateView(LoginRequiredMixin, UpdateView):

    model = Perfil
    success_url = reverse_lazy('Home')
    template_name = '/Home/perfil.html'
    fields = ['imagen', 'nombre', 'apellido', 'facebook', 'twitter', 'instagram', 'web', 'correo']