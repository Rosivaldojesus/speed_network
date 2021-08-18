from django.urls import path
from .views import Index, AdicionarNumeroVoip, ListaVoipDisponiveis,\
    ReservarNumeroVoip, ListaVoipReservados, FinalizarNumeroVoip,\
    ListaVoipFinalizados, VoipVisualizar

urlpatterns = [
    path('', Index),
    path('lista-voip-disponiveis/', ListaVoipDisponiveis),
    path('lista-voip-reservados/', ListaVoipReservados),
    path('lista-voip-finalizados/', ListaVoipFinalizados),
    path('reservar-numero-voip/<int:id>', ReservarNumeroVoip),
    path('finalizar-numero-voip/<int:id>', FinalizarNumeroVoip),
    path('visualizar-voip-finalizados/', VoipVisualizar),



    path('adicionar-numero-voip/', AdicionarNumeroVoip.as_view(), name='adicionar-numero-voip'),
    ]
