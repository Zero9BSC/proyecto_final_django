from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


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
            'email',
            'password1',
            'password2',
        ]

class UserEditForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        help_text = {k: '' for k in fields}

class AvatarEditForm():

    class Meta:
        model = Avatar
        fields = [
            'imagen',
            'nombre',
            'apellido',
            'facebook',
            'twitter',
            'instagram',
            'web',
            'correo',
        ]
        help_text = {k: '' for k in fields}