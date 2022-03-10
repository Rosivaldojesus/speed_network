from django.urls import path
from .views import Index
from .views import ManuaisServicos, login_user, submit_login, logout_user
from .views import Senhas, SenhasPorEquipamento, ManuaisVisualizacao, \
    CadastroSenhasPorEquipamentos, EditarSenhasPorEquipamentos, ExportarSenhasCSV
from .views import add_user

app_name = 'core'

urlpatterns = [
    path('', Index, name='core_index'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('login/submit', submit_login, name='login_submit'),
    path('senhas/', Senhas, name='senhas_gerais'),
    path('manuais/', ManuaisServicos, name='manuais_gerais'),
    path('manuais/manuais-visualizacao/', ManuaisVisualizacao, name='manuais_visualizacao'),
    path('senhas-por-equipamento/', SenhasPorEquipamento, name='senhas_por_equipamento'),
    path('cadastro-senhas-equipamentos/', CadastroSenhasPorEquipamentos, name='cadastro_senhas_equipamentos'),
    path('editar-senhas-equipamentos/<int:id>', EditarSenhasPorEquipamentos, name='editar_senhas_equipamentos'),
    path('exportar-senhas-csv/', ExportarSenhasCSV),
    path('novo-usuario/', add_user, name='add_user'),
]
