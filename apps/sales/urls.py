from django.urls import path
from .views import Index
from .views import CadastroInstalacao, InstalacaoVisualizacao, InstalacaoEditar,\
    InstalacaoAgendar, InstalacaoAberta, InstalacaoAgendada, InstalacaoFinalizar,\
    InstalacaoConcluida, InstalacaoSemBoleto, InstalacaoFinalizadaSemBoleto,\
    FinalizarEntregaBoleto, InstalacaoDefinirTecnico, VendasInstalacao, \
    InstalacaoConcluidaVendedores, DeletarInstalacaoAgendada, ClientesVoip, Voip


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
    path('instalacao-concluida-vendedores/', InstalacaoConcluidaVendedores),
    path('instalacao-aberta/', InstalacaoAberta),
    path('instalacao-agendada/', InstalacaoAgendada),
    path('instalacao-sem-boleto/', InstalacaoSemBoleto),
    path('instalacao-finalizada-sem-boleto/', InstalacaoFinalizadaSemBoleto),
    path('finalizar-boleto/<int:id>', FinalizarEntregaBoleto),
    path('definir-tecnico_instalacao/<int:id>', InstalacaoDefinirTecnico),

    path('vendas-instalacao/', VendasInstalacao),

    path('clientes-voip/', ClientesVoip),
    path('voip/', Voip),
    path('deletar-instalacao-agendada/<int:id>', DeletarInstalacaoAgendada),

    ]
