from django.urls import path
from .views import Index, AdicionarNumeroVoip, ListaVoipDisponiveis,\
    ReservarNumeroVoip, ListaVoipReservados, FinalizarNumeroVoip,\
    ListaVoipFinalizados, VoipVisualizar, SolicitarPortabilidadeVoip,\
    ListaVoipSemBoleto
from .views import FinalizarNumeroVoipSemBoleto


from .views import ListaPortabilidadeAguardando, PortabilidadeEnviarAnalise, ListaPortabilidadeAnalise

urlpatterns = [
    path('', Index),
    path('lista-voip-disponiveis/', ListaVoipDisponiveis),
    path('lista-voip-reservados/', ListaVoipReservados),
    path('lista-voip-sem-boleto/', ListaVoipSemBoleto),
    path('lista-voip-finalizados/', ListaVoipFinalizados),
    path('reservar-numero-voip/<int:id>', ReservarNumeroVoip),
    path('finalizar-numero-voip/<int:id>', FinalizarNumeroVoip),
    path('visualizar-voip-finalizados/', VoipVisualizar),

    path('finalizar-numero-voip-sem-boleto/<int:id>', FinalizarNumeroVoipSemBoleto),
    path('adicionar-numero-voip/', AdicionarNumeroVoip.as_view(), name='adicionar-numero-voip'),
    path('solicitar-portabilidade-voip/', SolicitarPortabilidadeVoip.as_view(), name='solicitar-portabilidade-voip'),

    path('lista-portabilidade-aguardando/', ListaPortabilidadeAguardando),
    path('lista-portabilidade-analise', ListaPortabilidadeAnalise),

    path('portabilidade-enviar-analise/<int:id>', PortabilidadeEnviarAnalise),


    ]
