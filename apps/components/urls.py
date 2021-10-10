from django.urls import path
from .views import Index, DirecionamentoServicos, RuasAtendidas, ExportarRuasCSV


urlpatterns = [
    path('', Index),
    path('direcionamento-servicos/', DirecionamentoServicos),
    path('ruas/', RuasAtendidas),
    path('exportar-ruas-csv/', ExportarRuasCSV)
    ]
