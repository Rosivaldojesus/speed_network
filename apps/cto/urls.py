from django.urls import path
from .views import Index, EditarCto, CtoCompletas, CTOCreate, CaixasEmenda,\
    CaixaEmendaVisualizacao, CadastrarCaixaEmenda, EditarCaixasEmendas, CaixaEmendaCreate,\
    Primaria, VisualizarCaixasPrimarias

from .views import PrimariasCreate

urlpatterns = [
    path('', Index),
    path('editar-terminais-opticos/<int:id>', EditarCto),
    path('cto-completas/', CtoCompletas),
    path('adicionar-cto/', CTOCreate.as_view(), name='adicionar-cto'),
    path('caixas-emenda/', CaixasEmenda),
    path('visualizar-caixa_emenda/', CaixaEmendaVisualizacao),
    path('cadastrar-caixas-emenda/', CadastrarCaixaEmenda),
    path('editar-caixas-emenda/<int:id>', EditarCaixasEmendas),

    path('cadastrar-caixa-emenda', CaixaEmendaCreate.as_view(), name='caixa-emenda-create'),

    path('primarias/', Primaria),

    path('adicionar-primaria/', PrimariasCreate.as_view(), name='adicionar-primaria'),
    path('caixas-primarias/', VisualizarCaixasPrimarias),



]