from django.urls import path
from .views import Index, EditarCto, CtoCompletas,  CaixasEmenda,\
    CaixaEmendaVisualizacao, CadastrarCaixaEmenda, EditarCaixasEmendas, \
    Primaria, VisualizarCaixasPrimarias

from .views import PrimariasCreate, CTOCreate, CaixasEmendaCreate

urlpatterns = [
    path('', Index),
    path('editar-terminais-opticos/<int:id>', EditarCto),
    path('cto-completas/', CtoCompletas),
    path('adicionar-cto/', CTOCreate.as_view(), name='adicionar-cto'),
    path('caixas-emenda/', CaixasEmenda),
    path('visualizar-caixa_emenda/', CaixaEmendaVisualizacao),
    path('cadastrar-caixas-emenda/', CadastrarCaixaEmenda),
    path('editar-caixas-emenda/<int:id>', EditarCaixasEmendas),

    path('criar-caixas-emenda/', CaixasEmendaCreate.as_view(), name='criar-caixas-emenda'),

    path('primarias/', Primaria),




    path('adicionar-primaria/', PrimariasCreate.as_view(), name='adicionar-primaria'),
    path('caixas-primarias/', VisualizarCaixasPrimarias),



]