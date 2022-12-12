from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm

class CrearPostForm(forms.ModelForm):
    
    class Meta:
        model= Post
        fields = '__all__'
        exclude = ["user"]

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = [
            'nombre',
            'email',
            'consulta',
        ]

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
        ]
        help_text = {k: '' for k in fields}

class PerfilForm(ModelForm):
    
    class Meta:
        model= Perfil
        fields = '__all__'
        exclude = ["usuario"]

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
        
