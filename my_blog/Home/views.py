from django.shortcuts import render, redirect
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


from .models import *
from .forms import *


# VISTAS BASADAS EN FUNCIONES
def mostrar_home(request):

    return render (request, "index.html")#, {'url': imagenes[0].imagen.url})

def buscar_post(request):
    
    return render(request, "buscar_post.html")

def buscar(request):

    try:
        if request.method == "GET":
            if request.GET["titulo"]:
                titulo = request.GET["titulo"]
                post = Post.objects.filter(titulo__icontains=titulo)
                if post:
                    
                    return render(request, "buscar_post.html", {"post":post, "titulo":titulo})    
                else:
                    
                    respuesta = "No hay post"
                
                    return render(request, "buscar_post.html", {"respuesta": respuesta})
    except ValueError:
        print('que haces hermano!? estas pasando algo sin valor flaco!')
        respuesta = "Debe ingresar un parametro para buscar"
        return render(request, "buscar_post.html", {"respuesta": respuesta})

def mostrar_post(request):
    return render(request, "post.html") #Solo como ejemplo para mostrar como se ve la template "post.html"

def mostrar_contacto(request):
    return render(request, "contacto.html")
    
def mostrar_about(request):
    return render(request, "about.html")

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
    perfil = Perfil.objects.get(usuario = request.user.id)
    usuario = request.user

    if request.method == 'POST':
        usuario_form = UserEditForm(request.POST)
        perfil_form = PerfilEditForm(request.POST)

        if usuario_form.is_valid() and perfil_form.is_valid():

            informacion1 = usuario_form.cleaned_data
            informacion2 = perfil_form.cleaned_data
            
            usuario.username = informacion1['username']
            usuario.password1 = informacion1['password1']
            usuario.password2 = informacion1['password2']
            usuario.save()

            perfil.imagen = informacion2['imagen']
            perfil.nombre = informacion2['nombre']
            perfil.apellido = informacion2['apellido']
            perfil.correo = informacion2['correo']
            perfil.facebook = informacion2['facebook']
            perfil.twitter = informacion2['twitter']
            perfil.instagram = informacion2['instagram']
            perfil.web = informacion2['web']
            perfil.save()


            return render(request, 'index.html')
        
    else:
        usuario_form = UserEditForm(initial={
            'username': usuario.username,
            'email': usuario.email,
        })
        perfil_form = PerfilEditForm(initial={
            'imagen': perfil.imagen,
            'nombre': perfil.nombre,
            'apellido': perfil.apellido,
            'correo': perfil.correo,
            'facebook': perfil.facebook,
            'twitter': perfil.twitter,
            'instagram': perfil.instagram,
            'web': perfil.web,
        })


    return render(request, 'admin_update.html', {
        'form': usuario_form,
        'form2': perfil_form,
        'usuario': usuario,
        })


def create_user(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        perfil_form = PerfilForm(request.POST)
        if user_form.is_valid() and perfil_form.is_valid():
            user = user_form.save()
            
            perfil = perfil_form.save(commit=False)
            perfil.usuario = User.objects.latest('id')

            print(f'el usuario {User.objects.latest("id").id}')
            
            perfil.save()

            return render(request, 'index.html')
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
    success_url = '/post_list' #posible solucion a crear post que no redirecciona bien al index

class PostUpdateView(LoginRequiredMixin, UpdateView):

    model = Post
    success_url = '/post_list' #posible solucion a crear post que no redirecciona bien al index
    fields = ['titulo', 'sub_titulo', 'fecha', 'texto']


class PostCreateView(LoginRequiredMixin, CreateView):

    model = Post
    success_url = '/post_list' #posible solucion a crear post que no redirecciona bien al index
    fields = ['titulo', 'sub_titulo', 'imagen', 'fecha', 'categoria', 'texto']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.autor = User.objects.get(id=self.request.user.id)  # use your own profile here
        post.save()
        return HttpResponseRedirect('/post_list')

class ContactCreateView(CreateView):

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
    #template_name = 'Home/post_gaming'

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
    #template_name = 'logout.html'

#class PerfilCreateView(CreateView):

    #form_class = PerfilCreateForm
    #success_url = reverse_lazy('Home')
    #template_name = '.html'

class PerfilUpdateView(LoginRequiredMixin, UpdateView):

    model = Perfil
    success_url = reverse_lazy('Home')
    template_name = '/Home/perfil.html'
    fields = ['imagen', 'nombre', 'apellido', 'facebook', 'twitter', 'instagram', 'web', 'correo']



