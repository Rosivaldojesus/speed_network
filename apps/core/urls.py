from django.urls import path
from .views import Index
from .views import ManuaisServicos, login

urlpatterns = [
    path('', Index),
    path('manuais/', ManuaisServicos),
    path('login/', login),
]