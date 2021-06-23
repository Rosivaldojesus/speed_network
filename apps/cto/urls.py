from django.urls import path
from .views import Index, EditarCto, CtoCompletas, CadastrarCto, InserirCto

urlpatterns = [
    path('', Index),
    path('cadastro-cto/', CadastrarCto),
    path('editar-terminais-opticos/<int:id>', EditarCto),
    path('cto-completas/', CtoCompletas),
    path('inserir-cto/', InserirCto),

]