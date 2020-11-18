from django.conf.urls import url
from . import views


urlpatterns = [
    url('', views.peliculas_lista, name ='peliculas_lista'),
    url(r'pelicula/nueva/', views.pelicula_nueva, name='pelicula_nueva'),
    ]