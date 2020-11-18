from django.shortcuts import render
from django.contrib import messages
from .forms import PeliculaForm
from pelicula.models import Pelicula, Actuacion

def pelicula_nueva(request):
    if request.method == "POST":
        formulario = PeliculaForm(request.POST)
        if formulario.is_valid():
            pelicula = Pelicula.objects.create(nombre=formulario.cleaned_data['nombre'], anio = formulario.cleaned_data['anio'])
            for actor_id in request.POST.getlist('actores'):
                actuacion = Actuacion(actor_id=actor_id, pelicula_id = pelicula.id)
                actuacion.save()
            messages.add_message(request, messages.SUCCESS, 'Pelicula Guardada Exitosamente')
    else:
        formulario = PeliculaForm()
    return render(request, 'pelicula/pelicula_nueva.html', {'formulario': formulario})

def peliculas_lista(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'pelicula/pelicula_lista.html', {'peliculas': peliculas})



