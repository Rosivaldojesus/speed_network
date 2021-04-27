from django.urls import path
from .views import Index, EntradaProdutos, SaidaProdutos

urlpatterns = [
    path('', Index),
    path('entrada-produtos/', EntradaProdutos),
    path('saida-produtos/', SaidaProdutos)
]