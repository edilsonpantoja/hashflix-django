from .models import Movie
# este arquivo eh um gerenciador de contexto
# usado pra que uma variavel possa ser acessado por todas as Views

# Pra que essas funcoes possam ser usadas pelo Django
# Eh preciso registra-las no arquivo settings.py do Django, no caso
# na pasta do hashflix
# na secao TEMPLATES

def lista_filmes_recentes(request):
    # lista com todos os filmes, o sinal de menos (-) significa ordem decrescente daquele campo
    lista_filmes = Movie.objects.all().order_by('-creation_date')[0:8]

    if lista_filmes:
        # pega a primeira posicao da lista
        filme_destaque = lista_filmes[0]
    else:
        filme_destaque = None
    #retorna uma tupla de um item so, com a lista dos filmes na ordem decrescente
    return {"lista_filmes_recentes": lista_filmes, "filme_destaque": filme_destaque}


def lista_filmes_emalta(request):
    lista_filmes = Movie.objects.all().order_by('-visualizations')[0:8]
    return {'lista_filmes_emalta': lista_filmes}

