from django.contrib import admin
from .models import Produto, EntradaProduto, SaidaProduto
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_produto', 'marca_produto', 'modelo_produto')
admin.site.register(Produto, ProdutoAdmin)


class EntradaProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantidade', 'produto')
admin.site.register(EntradaProduto, EntradaProdutoAdmin)


class SaidaProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantidade', 'produto')
admin.site.register(SaidaProduto)