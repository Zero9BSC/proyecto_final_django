from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

from .models import Post

@receiver(post_delete, sender=Post)
def eliminar_imagen_post(sender, instance, **kwargs):
    # Verifica si hay una imagen asociada y la elimina si existe
    if instance.imagen:
        if os.path.isfile(instance.imagen.path):
            os.remove(instance.imagen.path)
