from django.urls import path
from .views import Index, CadastroCto, EditarCto

urlpatterns = [
    path('', Index),
    path('cadastro-cto/', CadastroCto),
    path('editar-terminais-opticos/<int:id>', EditarCto)

]