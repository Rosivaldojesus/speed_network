from django.urls import path
from .views import Index, CadastroServico, AgendarServico, ServicosAbertos,\
    ServicosAgendados, ServicosFinalizados, EditarServico, RemoverServico,\
    EditarServicoAgendado, FinalizarServico


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

]