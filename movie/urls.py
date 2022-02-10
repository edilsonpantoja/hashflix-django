# url - view - template

from django.urls import path, include
from .views import Homefilmes, Homepage, Detalhesfilme


urlpatterns = [
    #path('', homepage),
    path('', Homepage.as_view()),
    path('movies/', Homefilmes.as_view()),
    path('movies/<int:pk>', Detalhesfilme.as_view())
]