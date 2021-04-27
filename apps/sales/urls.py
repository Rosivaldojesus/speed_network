from django.urls import path
from .views import Index, CadastroInstalacao, InstalacaoVisualizacao

urlpatterns = [
    #Instalação
    path('', Index),
    path('cadastro-instalacao/', CadastroInstalacao),
    path('visualizar-instalacao/', InstalacaoVisualizacao)
]