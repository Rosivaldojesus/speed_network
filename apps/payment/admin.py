from django.contrib import admin
from .models import CategoriaPagamento, Pagamento

# Register your models here.

admin.site.register(CategoriaPagamento)




class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('id','motivo_pagamento')
admin.site.register(Pagamento, PagamentoAdmin)
