from django.urls import path
from .views import Index, CadastrarPagamento
from .views import DashboardPagamentos, ListaPagamentos, AgendamentosPagamentos,\
    AgendarPagamento, ConfirmarPagamento, EditarPagamento, ExportarCSV,\
    PagamentosFuturos, PagamentosMensaisGrupos, FluxoEntradaSaida

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

    path('exportar-csv/', ExportarCSV),
]