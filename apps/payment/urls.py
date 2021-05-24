from django.urls import path
from .views import Index, CadastrarPagamento
from .views import DashboardPagamentos, TodosPagamentos

urlpatterns = [
    path('', Index),
    path('cadastrar-pagamento/', CadastrarPagamento),
    path('dashboard-pagamentos/', DashboardPagamentos),
    path('todos-pagamentos/', TodosPagamentos),
]