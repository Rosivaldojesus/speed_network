from django.contrib import admin
from .models import CategoriaPagamento, Pagamento, TipoCusto, OrigemValores

# Register your models here.

admin.site.register(CategoriaPagamento)
admin.site.register(TipoCusto)
admin.site.register(OrigemValores)




class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('id','motivo_pagamento')
admin.site.register(Pagamento, PagamentoAdmin)
