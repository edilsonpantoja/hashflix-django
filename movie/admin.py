from django.contrib import admin
from .models import Movie, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Movie)
admin.site.register(Episodio)

# o campo customizado na classe Usuarios nao aparece no administrativo do Django
# tem de criar uma lista (campos ex) onde o primeiro valor eh uma Tupla com nome da secao que aparece
# na pagina de administracao do usuario, ex: Personal info e o segundo valor eh um dicionario
# [
#       ("Personal info", {'field': ('Primeiro nome', 'Ultimo nome',)})
# ]
# tem que apendar o novo campo customizado
campos = list(UserAdmin.fieldsets)
campos.append(
    ("History", {'fields': ('filmes_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)

# Passando UserAdmin que eh da classe de Usuario do Django
admin.site.register(Usuario, UserAdmin)
