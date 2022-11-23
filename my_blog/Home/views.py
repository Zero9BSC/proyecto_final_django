from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import CrearPostForm, ContactoForm, SignUpForm


def mostrar_home(request):
    #queryset = request.GET.get("buscar")

    return render (request, "index.html")

def crear_post(request):
    if request.method == "POST":
        formulario = CrearPostForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

            post = Post(titulo=formulario_limpio["titulo"], sub_titulo=formulario_limpio["sub_titulo"], fecha=formulario_limpio["fecha"], texto=formulario_limpio["texto"])

            post.save()

            return render(request, "Home/templates/index.html")
    else:
        formulario = CrearPostForm()
        
        return render(request, "crear_post.html", {"formulario": formulario})

def buscar_post(request):
    print('aca no pasa naranja')
    return render(request, "buscar_post.html")

def buscar(request):

    if request.method == "GET":
        if request.GET["titulo"]:
            titulo = request.GET["titulo"]
            post = Post.objects.filter(titulo__icontains=titulo)
            if post:
                print('se encontro el resultado.....supuestamente')
                return render(request, "buscar_post.html", {"post":post, "titulo":titulo})    
            else:
                print('no hay resultado')
                respuesta = "No hay post"
            
        #    return HttpResponse(respuesta)
                return render(request, "buscar_post.html", {"respuesta": respuesta})


def mostrar_post(request):
    return render(request, "post.html") #Solo como ejemplo para mostrar como se ve la template "post.html"

def mostrar_contacto(request):
    return render(request, "contacto.html")
    
def mostrar_about(request):
    return render(request, "about.html")


def mostrar_noticias(request):
    post = Post.objects.all()

    
    all_entries = PostNoticias.objects.all()

    return render(request, "post_noticias.html", {"post":post})
    #return render(request, "post_noticias.html", {"all_entries": all_entries})

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

def eliminar_posteos(request, post_id):

    posteos = Post.objects.get(id=post_id)

    posteos.delete()

    posteos = Post.objects.all()

    context = {'posteos':posteos}

    return render(request, 'mostrar_posteos.html', context=context)


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

class PostDetailView(DetailView):

    model = Post
    template_name = 'Home/post_detalle.html'


class PostList(ListView):

    model = Post
    template_name = 'Home/post_list.html'

class PostDeleteView(DeleteView):

    model = Post
    success_url = '/post_list' #posible solucion a crear post que no redirecciona bien al index

class PostUpdateView(UpdateView):

    model = Post
    success_url = '/post_list' #posible solucion a crear post que no redirecciona bien al index
    fields = ['titulo', 'sub_titulo', 'fecha', 'texto']


class PostCreateView(CreateView):

    model = Post
    success_url = '/post_list' #posible solucion a crear post que no redirecciona bien al index
    fields = ['titulo', 'sub_titulo', 'fecha', 'texto']





#class SignUpView(CreateView):
#
#    form_class = SignUpForm
#    success_url = ''
#    template_name = 'registro.html'

