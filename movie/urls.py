# url - view - template
from django.urls import path, reverse_lazy
# importando os arquivos .html
from .views import Homefilmes, Homepage, Detalhesfilme, Pesquisafilme, Paginaperfil, Criarcontas
from django.contrib.auth import views as auth_view

app_name='movie'

urlpatterns = [
    #path('', homepage),
    path('', Homepage.as_view(), name='homepage'),
    path('movies/', Homefilmes.as_view(), name='homefilmes'),
    path('movies/<int:pk>', Detalhesfilme.as_view(), name='detalhesfilme'),
    path('search/', Pesquisafilme.as_view(), name='pesquisafilme'),
    # Django ja tem uma template pra login, precisa ser importada, ver auth_view acima
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/<int:pk>', Paginaperfil.as_view(), name='editarperfil'),
    path('criarconta/', Criarcontas.as_view(), name='criarconta'),
    # abaixo da pra aproveitar o mesmo html usado para alterar o perfil
    # usamos reverse_lazy pq aqui estamos passando como parametro no path
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name='editarperfil.html',
                                                             success_url=reverse_lazy('movie:homefilmes')), name='mudarsenha'),
]