from django.urls import path
from .views import Index
from .views import CadastroInstalacao, InstalacaoVisualizacao, InstalacaoEditar,\
    InstalacaoAgendar, InstalacaoAberta, InstalacaoAgendada, InstalacaoFinalizar,\
    InstalacaoConcluida


urlpatterns = [
      path('', Index),
    path('cadastro-instalacao/', CadastroInstalacao),
    path('instalacao-aberta/visualizar-instalacao/', InstalacaoVisualizacao),
    path('instalacao-agendada/visualizar-instalacao/', InstalacaoVisualizacao),
    path('instalacao-concluida/visualizar-instalacao/', InstalacaoVisualizacao),
    path('editar-instalacao/<int:id>', InstalacaoEditar),
    path('instalacao-agendada/editar-instalacao/<int:id>', InstalacaoEditar),
    path('agendar-instalacao/<int:id>', InstalacaoAgendar),
    path('finalizar-instalacao/<int:id>', InstalacaoFinalizar),
    path('instalacao-concluida/', InstalacaoConcluida),
    path('instalacao-aberta/', InstalacaoAberta),
    path('instalacao-agendada/', InstalacaoAgendada)
    ]
