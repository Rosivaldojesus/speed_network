from unittest import TestCase
from django.urls import reverse, resolve
from django.test import Client
from apps.core import views

# Create your tests here.

class CoreViewsTest(TestCase):
    def test_core_index_views_is_correct(self):
        view_index = resolve(reverse('core:core_index'))
        view_login = resolve(reverse('core:login'))
        self.assertIs(view_index.func, views.Index)
        self.assertIs(view_login.func, views.login_user)


    def test_core_login_views_is_correct(self):
        view_login = resolve(reverse('core:login'))
        self.assertIs(view_login.func, views.login_user)


"""
   
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
"""