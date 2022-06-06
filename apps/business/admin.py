from atexit import register
from django.contrib import admin
from .models import VendasProdutos

# Register your models here.

@admin.register(VendasProdutos)
class VendasProdutosAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'valor_unitario', 'valor_total')