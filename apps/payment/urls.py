from django.urls import path
from .views import Index, CadastrarPagamento
from .views import DashboardPagamentos, ListaPagamentos, AgendamentosPagamentos,\
    AgendarPagamento, ConfirmarPagamento, EditarPagamento, ExportarCSV,\
    PagamentosFuturos, PagamentosMensaisGrupos, FluxoEntradaSaida, FluxoCreate, ExportParaExcel

from .views import RetiradasGerencianetCreateView, RetiradasGerencianetUpdateView, RetiradasGerencianet

from .views import EntregaBoletosListView, EntregaBoletosCreateView
from .views import SalvarPagamento

urlpatterns = [
    path('', Index),
    path('cadastrar-pagamento/', CadastrarPagamento),
    path('dashboard-pagamentos/', DashboardPagamentos),
    path('lista-pagamentos/', ListaPagamentos),
    path('agendamentos-pagamentos/', AgendamentosPagamentos),
    path('agendar-pagamento/', AgendarPagamento),
    path('comfirmar-pagamento/<int:id>', ConfirmarPagamento),
    path('editar-pagamento/<int:id>', EditarPagamento),
    path('pagamentos-futuros/', PagamentosFuturos),
    path('pagamentos-mensais-grupos/', PagamentosMensaisGrupos),
    path('fluxo-entradas-saidas/', FluxoEntradaSaida),


    #ListView
    path('lista-entrega-boletos/', EntregaBoletosListView.as_view(), name='lista-entrega-boletos'),


    path('retiradas-gerencianet/', RetiradasGerencianet),



    #CreateView
    path('cadastrar-entrega-boletos/', EntregaBoletosCreateView.as_view(), name='cadastrar-entrega-boletos'),


    #path('retiradas-gerencianet/', RetiradasGerencianetListView.as_view(), name='retiradas-gerencianet'),
    path('cadastrar-valores-receitanet/', RetiradasGerencianetCreateView.as_view(), name='cadastrar-valores-receitanet'),

     # UpdateView
    path('retiradas-gerencianet/<slug:pk>/', RetiradasGerencianetUpdateView.as_view(), name='editar-valores-receitanet'),


    path('cadastrar-fluxo-entradas-saidas/', FluxoCreate.as_view(), name='cadastrar-fluxo-entradas-saidas'),

    path('salvar-pahemnto/', SalvarPagamento),

     path('exportar-csv/', ExportarCSV),
    path('exportar-excel/', ExportParaExcel),
    #path('exportar-excel/', ExportParaExcel().as_view(), name='exportar-excel'),
]