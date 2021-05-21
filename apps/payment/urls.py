from django.urls import path
from .views import Index, CadastrarPagamento
from .views import DashboardPagamentos

urlpatterns = [
    path('', Index),
    path('cadastrar-pagamento/', CadastrarPagamento),
    path('dashboard-pagamentos/', DashboardPagamentos),
]