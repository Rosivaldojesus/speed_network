from django.urls import path
from .views import Index, CadastroCto

urlpatterns = [
    path('', Index),
    path('cadastro-cto/', CadastroCto),

]