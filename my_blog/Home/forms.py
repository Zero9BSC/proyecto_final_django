from django import forms

class CrearPostForm(forms.Form):
    titulo = forms.CharField(max_length=90)
    sub_titulo = forms.CharField(max_length=90)
    fecha = forms.DateField()
    texto = forms.CharField(max_length=254)

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length= 90)
    email = forms.EmailField()
    consulta = forms.CharField(max_length=254)