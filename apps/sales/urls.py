from django.urls import path
from .views import Index
from .views import CadastroInstalacao, InstalacaoVisualizacao, InstalacaoEditar


urlpatterns = [
      path('', Index),
    path('cadastro-instalacao/', CadastroInstalacao),
    path('visualizar-instalacao/', InstalacaoVisualizacao),
    path('editar-instalacao/<int:id>', InstalacaoEditar),
]