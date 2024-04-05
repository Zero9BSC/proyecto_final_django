from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm


class CrearPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'sub_titulo', 'imagen', 'fecha', 'categoria', 'texto']

    def __init__(self, *args, **kwargs):
        super(CrearPostForm, self).__init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'Título'})
        self.fields['sub_titulo'].widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'Subtítulo'})
        self.fields['imagen'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['fecha'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['categoria'].widget.attrs.update({'class': 'form-control form-control-lg'})
        self.fields['texto'].widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'Texto'})


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'asunto', 'mensaje']


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password Again'
        })


class PerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'
        exclude = ["usuario"]
        widgets = {
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control form-control-lg'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Ingrese su nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Ingrese su apellido'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'example@example.com'}),
            'facebook': forms.URLInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'https://www.facebook.com/example'}),
            'twitter': forms.URLInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'https://twitter.com/example'}),
            'instagram': forms.URLInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'https://www.instagram.com/example/'}),
            'web': forms.URLInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'https://www.example.com'}),
        }


class UserEditForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))
    password2 = forms.CharField(label='Confirmación de contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}))

    class Meta:
        model = User
        fields = [
            'username',
        ]
        help_text = {k: '' for k in fields}

