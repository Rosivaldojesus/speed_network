from django.urls import path
from .views import Index
from .views import ManuaisServicos, login_user, submit_login, logout_user
from .views import Senhas, SenhasPorEquipamento, ManuaisVisualizacao, \
    CadastroSenhasPorEquipamentos, EditarSenhasPorEquipamentos, ExportarSenhasCSV
from .views import add_user

app_name = 'core'

urlpatterns = [
    path('', Index, name='core_index'),
    path('login/', login_user, name='core_login'),
    path('logout/', logout_user),



    path('novo-usuario/', add_user, name='add_user'),
    path('manuais/', ManuaisServicos),
    path('manuais/manuais-visualizacao/', ManuaisVisualizacao),


    path('login/submit', submit_login),
    path('senhas/', Senhas),
    path('senhas-por-equipamento/', SenhasPorEquipamento),
    path('cadastro-senhas-equipamentos/', CadastroSenhasPorEquipamentos),
    path('editar-senhas-equipamentos/<int:id>', EditarSenhasPorEquipamentos),
    path('exportar-senhas-csv/', ExportarSenhasCSV)
]
