from django.urls import path
from .views import Index, CadastrarPagamento

urlpatterns = [
    path('', Index),
    path('cadastrar-pagamento/', CadastrarPagamento),
]