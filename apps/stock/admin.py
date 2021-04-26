from django.contrib import admin
from .models import Produto
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_produto', 'marca_produto', 'modelo_produto')

admin.site.register(Produto, ProdutoAdmin)