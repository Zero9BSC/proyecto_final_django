from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm

class CrearPostForm(forms.ModelForm):
    
    class Meta:
        model= Post
        fields = '__all__'
        exclude = ["autor"]

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = [
            'nombre',
            'email',
            'consulta',
        ]

# class SignUpForm(UserCreationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))
    
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2']
#         help_text = {k: '' for k in fields}
        
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
        model= Perfil
        fields = '__all__'
        exclude = ["usuario"]
        widgets = {
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@example.com'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese su apellido'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'facebook': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://www.facebook.com/example'}),
            'twitter': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://twitter.com/example'}),
            'instagram': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://www.instagram.com/example/'}),
            'web': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://www.example.com'}),
        }

class UserEditForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
        ]
        help_text = {k: '' for k in fields}

class PerfilEditForm(ModelForm):

    class Meta:
        model= Perfil
        fields = '__all__'
        exclude = ["usuario"]
        help_text = {k: '' for k in fields}
        
