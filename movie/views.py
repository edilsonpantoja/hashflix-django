from django.shortcuts import render
from .models import Movie
from django.views.generic import TemplateView, ListView, DetailView


class Homepage(TemplateView):
    template_name = "homepage.html"


class Homefilmes(ListView):
    template_name = "homefilmes.html"
    model = Movie
    #object_list -> lista de itens do modelo
    #o object_list vai ser passado pro html com a lista dos dados do Modelo Movie
    #quando se usa classe nao precisa passar context automaticamente o django gerencia varias coisas


class Detalhesfilme(DetailView):
    template_name = "detalhesfilme.html"
    model = Movie
    # object -> 1 item do nosso modelo

    # o codigo abaixo serve pra passar uma variavel pra uma view especifica
    # no caso utiliza-se a funcao get_context_data
    # na primeira linha da funcaco, declara-se context igual a super classe
    # se isso nao for feito, a funcao get_context_data ira sobrescrever as instrucoes
    # da super classe
    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        # filtrar a minha tabela de filmes pegando os filmes cuja categoria eh igual
        # a categoria do filme da pagina (object)
        # self.get_object()
        # todos os filmes cuja categoria eh igual a categoria do filme que estamos acessando
        # filmes_relacionados = Movie.objects.filter(category=self.get_object().category)[0:5] pega so 5 filmes
        filmes_relacionados = Movie.objects.filter(category=self.get_object().category)
        context["filmes_relacionados"] = filmes_relacionados
        return context

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