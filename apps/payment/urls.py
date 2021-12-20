from django.urls import path
from .views import Index, CadastrarPagamento
from .views import DashboardPagamentos, ListaPagamentos, AgendamentosPagamentos,\
    AgendarPagamento, ConfirmarPagamento, EditarPagamento, ExportarCSV,\
    PagamentosFuturos, PagamentosMensaisGrupos, FluxoEntradaSaida, FluxoCreate

from .views import RetiradasGerencianetCreateView, RetiradasGerencianetUpdateView, RetiradasGerencianet

from .views import EntregaBoletosListView, EntregaBoletosCreateView, EditarEntregaBoletosUpdateView
from .views import SalvarPagamento

from .views import IndexTemplateView, CustoMensalCategoriaView, FluxoEntradaSaidaView


urlpatterns = [
    #  Refatorado
    path('indexx/', IndexTemplateView.as_view(), name='indexx'),
    path('custo-mensal-categoria', CustoMensalCategoriaView.as_view(), name='custo_mensal_categoria'),
    path('fluxo-entrada-saida', FluxoEntradaSaidaView.as_view(), name='fluxo_entrada_saida'),


    #  Pré-Refatorado
    path('lista-pagamentos/', ListaPagamentos, name='lista_pagamentos'),





    # Sem refatoração
    path('', Index),
    path('cadastrar-pagamento/', CadastrarPagamento),

    path('dashboard-pagamentos/', DashboardPagamentos),

    path('agendamentos-pagamentos/', AgendamentosPagamentos),
    path('agendar-pagamento/', AgendarPagamento),
    path('comfirmar-pagamento/<int:id>', ConfirmarPagamento),
    path('editar-pagamento/<int:id>', EditarPagamento),
    path('pagamentos-futuros/', PagamentosFuturos),
    path('pagamentos-mensais-grupos/', PagamentosMensaisGrupos),
    path('fluxo-entradas-saidas/', FluxoEntradaSaida),

    #  ListView
    path('lista-entrega-boletos/', EntregaBoletosListView.as_view(), name='lista-entrega-boletos'),
    path('editar-entrega-boletos/<int:pk>', EditarEntregaBoletosUpdateView.as_view(), name='editar-entrega-boletos'),

    path('retiradas-gerencianet/', RetiradasGerencianet),

    #  CreateView
    path('cadastrar-entrega-boletos/', EntregaBoletosCreateView.as_view(), name='cadastrar-entrega-boletos'),

    #  path('retiradas-gerencianet/', RetiradasGerencianetListView.as_view(), name='retiradas-gerencianet'),
    path('cadastrar-valores-receitanet/', RetiradasGerencianetCreateView.as_view(),
         name='cadastrar-valores-receitanet'),

    # UpdateView
    path('retiradas-gerencianet/<int:pk>/', RetiradasGerencianetUpdateView.as_view(),
         name='editar-valores-receitanet'),

    path('cadastrar-fluxo-entradas-saidas/', FluxoCreate.as_view(), name='cadastrar-fluxo-entradas-saidas'),

    path('salvar-pahemnto/', SalvarPagamento),

    path('exportar-csv/', ExportarCSV),
]
