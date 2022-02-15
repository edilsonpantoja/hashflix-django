# url - view - template

from django.urls import path, include
from .views import Homefilmes, Homepage, Detalhesfilme, Pesquisafilme
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
]