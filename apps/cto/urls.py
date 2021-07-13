from django.urls import path
from .views import Index, EditarCto, CtoCompletas, InsertCto, CaixasEmenda,\
    CaixaEmendaVisualizacao, CadastrarCaixaEmenda, EditarCaixasEmendas

urlpatterns = [
    path('', Index),
    path('editar-terminais-opticos/<int:id>', EditarCto),
    path('cto-completas/', CtoCompletas),
    path('add-cto/', InsertCto),
    path('caixas-emenda/', CaixasEmenda),
    path('visualizar-caixa_emenda/', CaixaEmendaVisualizacao),
    path('cadastrar-caixas-emenda/', CadastrarCaixaEmenda),
    path('editar-caixas-emenda/<int:id>', EditarCaixasEmendas),


]