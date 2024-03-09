# En el archivo __init__.py dentro del directorio templatetags de la aplicación Home
from django import template
from .custom_filters import add_class

register = template.Library()
register.filter('add_class', add_class)
