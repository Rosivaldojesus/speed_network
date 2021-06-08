from django.urls import path
from .views import Index, DirecionamentoServicos


urlpatterns = [
    path('', Index),
    path('direcionamento-servicos/', DirecionamentoServicos),

    ]
