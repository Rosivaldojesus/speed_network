from django.urls import path
from .views import Index, DirecionamentoServicos, RuasAtendidas


urlpatterns = [
    path('', Index),
    path('direcionamento-servicos/', DirecionamentoServicos),

    path('ruas/', RuasAtendidas),

    ]
