from django.urls import path
from .views import Index, CadastroServico, AgendarServico, ServicosAbertos, ServicosAgendados, ServicosFinalizados,\
    EditarServico, RemoverServico, EditarServicoAgendado, FinalizarServico, ServicoVisualizar, ServicosVoip,\
    ServicosVoipDisponiveis, ReservarVoip, ServicosVoipReservados, DeletarServico, ReservarVoipPortabilidadeCreate
from .views import servicos_de_retiradas, servicos_retiradas_agendados
from .views import relatorio_servicos_retiradas




urlpatterns = [


    path('', Index),
    path('cadastro-servico/', CadastroServico),
    path('editar-servico/<int:id>', EditarServico),
    path('remover-servico/<int:id>', RemoverServico),
    path('servicos-abertos/', ServicosAbertos),
    path('agendar-servico/<int:id>', AgendarServico),
    path('servicos-agendados/', ServicosAgendados),
    path('editar-servico-agendado/<int:id>', EditarServicoAgendado),
    path('servicos-finalizados/', ServicosFinalizados),
    path('finalizar-servico/<int:id>', FinalizarServico),
    path('visualizar-servico/', ServicoVisualizar),

    path('servicos-voip/', ServicosVoip),
    path('servicos-voip-disponiveis/', ServicosVoipDisponiveis),
    path('reservar-voip/<int:id>', ReservarVoip),
    path('servicos-voip-reservados/', ServicosVoipReservados),

    path('deletar-servico/<int:id>', DeletarServico),

    path('reservar-voip-portabilidade/', ReservarVoipPortabilidadeCreate.as_view(), name='reservar-voip-portabilidade'),


    path('servicos-de-retiradas-agendados/', servicos_retiradas_agendados, name='servicos-de-retiradas-agendados'),

    path('servicos-de-retiradas/', servicos_de_retiradas, name='servicos-de-retiradas'),

    path('relatorio-servicos-retiradas/', relatorio_servicos_retiradas, name='exportar_servicos_em_analise'),



]


