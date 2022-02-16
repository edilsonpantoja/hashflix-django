from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class CriarContaForm(UserCreationForm):
    email = forms.EmailField() #campo customizado, nao faz parte do padrao do django

    class Meta: #tem de usar essa classe Meta
        model = Usuario #eh a nossa classe Usuario que estamos usando pra personalizar
        fields = ('username', 'email', 'password1', 'password2')