from django.shortcuts import render, redirect
from .models import Movie
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# LoginRequiredMixin tem de ser a primeira classe criada em uma View
# Isso pra poder bloquear as views para usuarios nao logados

class Homepage(TemplateView):
    template_name = "homepage.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # se o usuario estiver logado, redireciona para a homefimes (urls.py)
            return redirect('movie:homefilmes')
        else:
            return super().get(request, *args, **kwargs)  # redireciona o usuario para a homepage


class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Movie
    #object_list -> lista de itens do modelo
    #o object_list vai ser passado pro html com a lista dos dados do Modelo Movie
    #quando se usa classe nao precisa passar context automaticamente o django gerencia varias coisas


class Detalhesfilme(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    model = Movie
    # object -> 1 item do nosso modelo

    # Funcao pra contar as Visualizacoes
    # toda funcao get precisa conter esses 4 argumentos
    def get(self, request, *args, **kwargs):
        # descobrir qual o filme ele esta acessando
        # contabilizar a visualizacao
        movie = self.get_object()
        # somar 1 nas visualizadoes daquele filme
        movie.visualizations += 1
        # salvar
        movie.save()
        # adicionar movie na lista de filmes assistidos pelo usuario
        usuario = request.user
        #adiciona o movie no banco de dados
        usuario.filmes_vistos.add(movie)
        return super().get(request, *args, **kwargs) #redireciona o usuario para a url final


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
        # context eh um dicionario
        filmes_relacionados = Movie.objects.filter(category=self.get_object().category)
        context["filmes_relacionados"] = filmes_relacionados
        return context

#pra criar uma View eh precisa
#passar um Model e um Template
class Pesquisafilme(ListView):
    template_name = "pesquisa.html"
    model = Movie

    # funcao pra pegar o paramentro query que eh o nome
    # da tag input na pagina homepage.html
    # pega o que foi digitado no campo de pesquisa pelo usuario
    # a funcao abaixo editando o object_list
    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            # object_list eh o nome padrao dado para a Listview
            #title__icontains onde title eh o nome do campo + '__icontains'
            # ao inves de usar 'Movie', podemos usar a variavel model que esta
            # declarada acima aqui nesta funcao, dessa forma, no futuro se precisarmos
            # mudamos o nome do model de Movie para Episodios, por exemplo
            # em um so lugar e nao em varios lugares na funcao
            #object_list = Movie.objects.filter(title__icontains=termo_pesquisa)
            object_list = self.model.objects.filter(title__icontains=termo_pesquisa)
            return object_list
        else:
            return None


class Paginaperfil(LoginRequiredMixin, TemplateView):
    template_name = "editarperfil.html"


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