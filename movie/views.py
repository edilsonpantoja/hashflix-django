from django.shortcuts import render
from .models import Movie

# Create your views here.
def homepage(request):
    return render(request, "homepage.html")


#url - view - html
def homefilmes(request):
    """
    Criar um context pra passar como terceiro argumento na funcao render
    Criar um dicionario, uma lista que vai conter informacoes do database
    para ser passado na funcao

    lista_filmes eh a chave do dicionario que eh passada com o mesmo nome da variavel
    """
    context = {}
    lista_filmes = Movie.objects.all()
    context['lista_filmes'] =  lista_filmes
    return render(request, "homefilmes.html", context)