from django.urls import path
from .views import Index, CadastrarPagamento, Home
from .views import DashboardPagamentos, ListaPagamentos, AgendamentosPagamentos,\
    AgendarPagamento, ConfirmarPagamento, EditarPagamento, ExportarCSV,\
    PagamentosFuturos, PagamentosMensaisGrupos, FluxoEntradaSaida, FluxoCreate

from .views import RetiradasGerencianetCreateView, RetiradasGerencianetUpdateView, RetiradasGerencianet

from .views import EntregaBoletosListView, EntregaBoletosCreateView, EditarEntregaBoletosUpdateView
from .views import SalvarPagamento


from .views import IndexTemplateView




urlpatterns = [
    path('indexx/', IndexTemplateView.as_view(), name='indexx'),





    path('', Index),
    path('cadastrar-pagamento/', CadastrarPagamento),
    path('home/', Home),
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
    path('editar-entrega-boletos/<int:pk>', EditarEntregaBoletosUpdateView.as_view(), name='editar-entrega-boletos'),

    path('retiradas-gerencianet/', RetiradasGerencianet),

    #CreateView
    path('cadastrar-entrega-boletos/', EntregaBoletosCreateView.as_view(), name='cadastrar-entrega-boletos'),

    #path('retiradas-gerencianet/', RetiradasGerencianetListView.as_view(), name='retiradas-gerencianet'),
    path('cadastrar-valores-receitanet/', RetiradasGerencianetCreateView.as_view(), name='cadastrar-valores-receitanet'),

     # UpdateView
    path('retiradas-gerencianet/<int:pk>/', RetiradasGerencianetUpdateView.as_view(), name='editar-valores-receitanet'),

    path('cadastrar-fluxo-entradas-saidas/', FluxoCreate.as_view(), name='cadastrar-fluxo-entradas-saidas'),

    path('salvar-pahemnto/', SalvarPagamento),

     path('exportar-csv/', ExportarCSV),

    #path('exportar-excel/', ExportParaExcel().as_view(), name='exportar-excel'),
]