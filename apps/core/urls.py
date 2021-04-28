from django.urls import path
from .views import Index
from .views import ManuaisServicos

urlpatterns = [
    path('', Index),
    path('manuais/', ManuaisServicos)
]