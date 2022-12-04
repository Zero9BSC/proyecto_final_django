from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required # DECORATORS para vistas basadas en Funciones
from django.contrib.auth.mixins import LoginRequiredMixin # MIXINS para vistas basadas en Clases


from .models import *
from .forms import CrearPostForm, ContactoForm, SignUpForm, UserEditForm


# VISTAS BASADAS EN FUNCIONES
def mostrar_home(request):

    #imagenes = Avatar.objects.filter(user=request.user.id)

    return render (request, "index.html")#, {'url': imagenes[0].imagen.url})

@login_required
def crear_post(request):
    if request.method == "POST":
        formulario = CrearPostForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            post = Post(titulo=formulario_limpio["titulo"], imagen=formulario_limpio["imagen"], sub_titulo=formulario_limpio["sub_titulo"], autor=formulario_limpio["autor"], fecha=formulario_limpio["fecha"], texto=formulario_limpio["texto"])

            post.save()

            return render(request, "Home/templates/index.html")
    else:
        formulario = CrearPostForm()
        
        return render(request, "crear_post.html", {"formulario": formulario})

def buscar_post(request):
    
    return render(request, "buscar_post.html")

def buscar(request):

    if request.method == "GET":
        if request.GET["titulo"]:
            titulo = request.GET["titulo"]
            post = Post.objects.filter(titulo__icontains=titulo)
            if post:
                
                return render(request, "buscar_post.html", {"post":post, "titulo":titulo})    
            else:
                
                respuesta = "No hay post"
            
                return render(request, "buscar_post.html", {"respuesta": respuesta})


def mostrar_post(request):
    return render(request, "post.html") #Solo como ejemplo para mostrar como se ve la template "post.html"

def mostrar_contacto(request):
    return render(request, "contacto.html")
    
def mostrar_about(request):
    return render(request, "about.html")


#def mostrar_noticias(request):
#    post = Post.objects.all()
#
#    
#    all_entries = Post.objects.filter()
#
#    return render(request, "post_noticias.html", {"post":post})
#    #return render(request, "post_noticias.html", {"all_entries": all_entries})

def crear_consulta(request):
    if request.method == "POST":
        formulario = ContactoForm(request.Contacto)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            contacto = Contacto(nombre=formulario_limpio["nombre"], email=formulario_limpio["email"], consulta=formulario_limpio["consulta"])

            contacto.save()

            return render(request, "Home/templates/index.html")
    else:
        formulario = ContactoForm()
        
    return render(request, "contacto.html", {"formulario": formulario})

def mostrar_posteos(request):

    posteos = Post.objects.all()

    context = {'posteos':posteos}

    return render(request, 'mostrar_posteos.html', context=context)

@login_required
def eliminar_posteos(request, post_id):

    posteos = Post.objects.get(id=post_id)

    posteos.delete()

    posteos = Post.objects.all()

    context = {'posteos':posteos}

    return render(request, 'mostrar_posteos.html', context=context)

@login_required
def actualizar_posteos(request, post_id):

    post = Post.objects.get(id=post_id)

    if request.method == "POST":

        formulario = CrearPostForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            #post = Post(titulo=formulario_limpio["titulo"], sub_titulo=formulario_limpio["sub_titulo"], fecha=formulario_limpio["fecha"], texto=formulario_limpio["texto"])

            post.titulo = formulario_limpio['titulo']
            post.sub_titulo = formulario_limpio['sub_titulo']
            post.fecha = formulario_limpio['fecha']
            post.texto = formulario_limpio['texto']
            
            post.save()

            return render(request, "Home/templates/index.html")
    else:
        formulario = CrearPostForm(initial={'titulo': post.titulo, 'sub_titulo': post.sub_titulo, 'fecha': post.fecha, 'texto': post.texto})
        
        return render(request, "actualizar_post.html", {"formulario": formulario})

@login_required
def editar_usuario(request):

    usuario = request.user

    if request.method == 'POST':
        usuario_form = UserEditForm(request.POST)

        if usuario_form.is_valid():

            informacion = usuario_form.cleaned_data
            
            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']

            usuario.save()

            return render(request, 'index.html')
        
    else:
        usuario_form = UserEditForm(initial={
            'username': usuario.username,
            'email': usuario.email,
        })

    return render(request, 'admin_update.html', {
        'form': usuario_form,
        'usuario': usuario
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
    success_url = '/post_list' #posible solucion a crear post que no redirecciona bien al index

class PostUpdateView(LoginRequiredMixin, UpdateView):

    model = Post
    success_url = '/post_list' #posible solucion a crear post que no redirecciona bien al index
    fields = ['titulo', 'sub_titulo', 'fecha', 'texto']


class PostCreateView(LoginRequiredMixin, CreateView):

    model = Post
    success_url = '/post_list' #posible solucion a crear post que no redirecciona bien al index
    fields = ['titulo', 'sub_titulo', 'imagen', 'fecha', 'categoria', 'texto']


class ContactCreateView(CreateView):

    form_class = ContactoForm
    template_name = 'contacto.html'
    success_url = reverse_lazy('Home')

class PostListGaming(ListView):
    model = Post
    template_name = 'Home/post_gaming'

class SignUpView(CreateView):

    form_class = SignUpForm
    success_url = reverse_lazy('Home')
    template_name = 'registro.html'

class AdminLoginView(LoginView):
    template_name = 'login.html'

class AdminLogoutView(LogoutView):
    success_url = reverse_lazy('Home')
    template_name = 'logout.html'


class AvatarUpdateView(LoginRequiredMixin, UpdateView):

    model = Avatar
    #success_url = reverse_lazy('Home')
    template_name = 'perfil.html'
    fields = ['imagen', 'nombre', 'apellido', 'facebook', 'twitter', 'instagram', 'web', 'correo']


#class AutorUpdateView(LoginRequiredMixin, UpdateView):
#
#    model = Autor
#    success_url = '/index' #posible solucion a crear post que no redirecciona bien al index
#    fields = [
#        'nombres', 
#        'apellidos', 
#        'facebook', 
#        'twitter', 
#        'instagram', 
#        'web', 
#        'correo', 
#        'estado',
#    ]


