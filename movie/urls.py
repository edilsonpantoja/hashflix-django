# url - view - template

from django.urls import path, include
from .views import Homefilmes, Homepage, Detalhesfilme

app_name='movie'

urlpatterns = [
    #path('', homepage),
    path('', Homepage.as_view(), name='homepage'),
    path('movies/', Homefilmes.as_view(), name='homefilmes'),
    path('movies/<int:pk>', Detalhesfilme.as_view(), name='detalhesfilme')
]