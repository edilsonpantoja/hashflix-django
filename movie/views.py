from django.shortcuts import render
from .models import Movie
from django.views.generic import TemplateView, ListView, DetailView


class Homepage(TemplateView):
    template_name = "homepage.html"


class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Movie
    #object_list
    #o object_list vai ser passado pro html com a lista dos dados do Modelo Movie
    #quando se usa classe nao precisa passar context automaticamente o django gerencia varias coisas


class Detalhesfilme(DetailView):
    template_name = "detalhesfilme.html"
    model = Movie
    # object -> 1 item do nosso modelo


# Create your views here.
#def homepage(request):
#    return render(request, "homepage.html")


#url - view - html
# def homefilmes(request):
#     """
#     Criar um context pra passar como terceiro argumento na funcao render
#     Criar um dicionario, uma lista que vai conter informacoes do database
#     para ser passado na funcao
#
#     lista_filmes eh a chave do dicionario que eh passada com o mesmo nome da variavel
#     """
#     context = {}
#     lista_filmes = Movie.objects.all()
#     context['lista_filmes'] =  lista_filmes
#     return render(request, "homefilmes.html", context)