from django.contrib import admin
from django.urls import path, re_path, include
from my_blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('Home.urls')),
]