from django.contrib import admin

from django.contrib import admin
from pelicula.models import Actor, ActorAdmin, Pelicula, PeliculaAdmin

admin.site.register(Actor, ActorAdmin)
admin.site.register(Pelicula, PeliculaAdmin)

