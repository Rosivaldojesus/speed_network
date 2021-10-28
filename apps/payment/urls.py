from django.urls import path
from .views import Index, CadastrarPagamento
from .views import DashboardPagamentos, ListaPagamentos, AgendamentosPagamentos,\
    AgendarPagamento, ConfirmarPagamento, EditarPagamento, ExportarCSV,\
    PagamentosFuturos, PagamentosMensaisGrupos, FluxoEntradaSaida, FluxoCreate, ExportParaExcel

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
    path('cadastrar-fluxo-entradas-saidas/', FluxoCreate.as_view(), name='cadastrar-fluxo-entradas-saidas'),

    path('salvar-pahemnto/', SalvarPagamento),

     path('exportar-csv/', ExportarCSV),
    path('exportar-excel/', ExportParaExcel),
    #path('exportar-excel/', ExportParaExcel().as_view(), name='exportar-excel'),
]