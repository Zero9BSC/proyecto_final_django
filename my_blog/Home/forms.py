from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CrearPostForm(forms.Form):
    titulo = forms.CharField(max_length=90)
    sub_titulo = forms.CharField(max_length=90)
    fecha = forms.DateField()
    categoria = forms.CharField(max_length=20)
    texto = forms.CharField(max_length=254)

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length= 90)
    email = forms.EmailField()
    consulta = forms.CharField(max_length=254)


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
