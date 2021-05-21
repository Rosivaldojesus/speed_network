from django.urls import path
from .views import Index
from .views import ManuaisServicos, login
from .views import Senhas, SenhasPorEquipamento, ManuaisVisualizacao

urlpatterns = [
    path('', Index),
    path('manuais/', ManuaisServicos),
    path('manuais/manuais-visualizacao/', ManuaisVisualizacao),
    path('login/', login),
    path('senhas/', Senhas),
    path('senhas-por-equipamento/', SenhasPorEquipamento),
]