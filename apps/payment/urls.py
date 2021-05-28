from django.urls import path
from .views import Index, CadastrarPagamento
from .views import DashboardPagamentos, TodosPagamentos, AgendamentosPagamentos, AgendarPagamento, ConfirmarPagamento

urlpatterns = [
    path('', Index),
    path('cadastrar-pagamento/', CadastrarPagamento),
    path('dashboard-pagamentos/', DashboardPagamentos),
    path('todos-pagamentos/', TodosPagamentos),
    path('agendamentos-pagamentos/', AgendamentosPagamentos),
    path('agendar-pagamento/', AgendarPagamento),
    path('comfirmar-pagamento/<int:id>', ConfirmarPagamento),
]