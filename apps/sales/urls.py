from django.urls import path
from .views import Index, CadastroInstalacao

urlpatterns = [
    #Instalação
    path('', Index),
    path('cadastro-instalacao/', CadastroInstalacao)
]