from django.urls import path
from .views import Index
from .views import ManuaisServicos, login
from .views import Senhas

urlpatterns = [
    path('', Index),
    path('manuais/', ManuaisServicos),
    path('login/', login),
    path('senhas/', Senhas),
]