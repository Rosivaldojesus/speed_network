from django.urls import path
from .views import VendasView, VendaCreateView, VendaDetailView, VendaUpdateView,\
ConcluirVendaUpdateView, HistoricoVendaListView

urlpatterns = [
    path('', VendasView.as_view(), name='venda_produtos'),

    path('historico-vendas', HistoricoVendaListView.as_view(), name='historico_vendas'),


    path('cadastar-venda/', VendaCreateView.as_view(), name='cadastrar_venda'),
    path('<int:pk>/', VendaDetailView.as_view(), name='detalhe_venda'),
    path('editar/<int:pk>/', VendaUpdateView.as_view(), name='editar_venda'),
    path('concluir-venda/<int:pk>/', ConcluirVendaUpdateView.as_view(), name='concluir_venda'),
]