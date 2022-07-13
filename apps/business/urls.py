from django.urls import path
from .views import VendasView, VendaCreateView, VendaDetailView, VendaUpdateView,\
ConcluirVendaUpdateView, HistoricoVendaListView

from .views import ComprasView, CompraCreateView, CompraUpdateView, HistoricoCompraListView, \
    CompraDetailView, ConcluirCompraUpdateView

urlpatterns = [

    # Urls das Informações de compras
    path('vendas/', VendasView.as_view(), name='venda_produtos'),
    path('historico-vendas/', HistoricoVendaListView.as_view(), name='historico_vendas'),
    path('cadastar-venda/', VendaCreateView.as_view(), name='cadastrar_venda'),
    path('detalhe-venda/<int:pk>/', VendaDetailView.as_view(), name='detalhe_venda'),
    path('editar-venda/<int:pk>/', VendaUpdateView.as_view(), name='editar_venda'),
    path('concluir-venda/<int:pk>/', ConcluirVendaUpdateView.as_view(), name='concluir_venda'),

    # Urls das Informações de compras
    path('compras/', ComprasView.as_view(), name='compra_produtos'),
    path('cadastar-compra/', CompraCreateView.as_view(), name='cadastrar_compra'),
    path('detalhe-compra/<int:pk>/', CompraDetailView.as_view(), name='detalhe_compra'),
    path('editar-compra/<int:pk>/', CompraUpdateView.as_view(), name='editar_compra'),
    path('concluir-compra/<int:pk>/', ConcluirCompraUpdateView.as_view(), name='concluir_compra'),
    path('historico-compras/', HistoricoCompraListView.as_view(), name='historico_compras'),
]