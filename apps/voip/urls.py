from django.urls import path
from .views import Index, AdicionarNumeroVoip, ListaVoipDisponiveis,\
    ReservarNumeroVoip, ListaVoipReservados, FinalizarNumeroVoip,\
    ListaVoipFinalizados, VoipVisualizar, SolicitarPortabilidadeVoip,\
    ListaVoipSemBoleto, SolicitarNumeroVoip, ListaVoipSolicitados
from .views import FinalizarNumeroVoipSemBoleto


from .views import ListaPortabilidadeAguardando, PortabilidadeEnviarAnalise,\
    ListaPortabilidadeAnalise, FinalizarPortabiliadeVoip, ListaPortabilidadeFinalizados

urlpatterns = [
    path('', Index),
    path('lista-voip-disponiveis/', ListaVoipDisponiveis),
    path('lista-voip-reservados/', ListaVoipReservados),
    path('lista-voip-solicitados/', ListaVoipSolicitados),
    path('lista-voip-sem-boleto/', ListaVoipSemBoleto),
    path('lista-voip-finalizados/', ListaVoipFinalizados),
    path('reservar-numero-voip/<int:id>', ReservarNumeroVoip),
    path('finalizar-numero-voip/<int:id>', FinalizarNumeroVoip),
    path('visualizar-voip-finalizados/', VoipVisualizar),
    path('solicitar-numero-voip/', SolicitarNumeroVoip.as_view(), name='solicitar-numero-voip'),


    path('finalizar-numero-voip-sem-boleto/<int:id>', FinalizarNumeroVoipSemBoleto),
    path('adicionar-numero-voip/', AdicionarNumeroVoip.as_view(), name='adicionar-numero-voip'),
    path('solicitar-portabilidade-voip/', SolicitarPortabilidadeVoip.as_view(), name='solicitar-portabilidade-voip'),

    path('lista-portabilidade-aguardando/', ListaPortabilidadeAguardando),
    path('lista-portabilidade-analise/', ListaPortabilidadeAnalise),
    path('portabilidade-enviar-analise/<int:id>', PortabilidadeEnviarAnalise),
    path('finalizar-portabilidade-voip/<int:id>', FinalizarPortabiliadeVoip),
    path('lista-portabilidade-finalizados/', ListaPortabilidadeFinalizados),


    ]
