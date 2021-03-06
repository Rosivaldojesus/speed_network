from django.urls import path
from .views import *
from . import views

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

    path('deletar-instalacao-agendada/<int:id>', DeletarInstalacaoAgendada),

    path('vale-refeicao/', ValeRefeicoes),
    path('adicionar-valor-vale/<int:id>', AdicionarValorVale),
    path('adicionar-pagamento-vale/<int:id>', AdicionarPagamentoVale),

    path('emitir-vale-refeicao/', EmitirValeRefeicaoCreate.as_view(), name='emitir-vale-refeicao'),
    path('adicionar_nome-para-vale/', AdicionarNomeParaValeCreate.as_view(), name='adicionar_nome-para-vale'),

    # ------------- Cancellations ----------------
    path('criar-cancelamento/', CancelamentosCreateView.as_view(), name='criar-cancelamento'),
    path('lista-cancelamentos/', CancelamentosListView.as_view(), name='lista-cancelamentos'),

    # UpdateView
    path('editar-cancelamento/<int:pk>', CancelamentosUpdateView.as_view(), name='editar-cancelamento'),

    # Relatórios em CSV
    path('ExportarReletarioVendasVendedor', ExportarReletarioVendasVendedor, name='exportar-reletario-vendas-vendedor')
]
