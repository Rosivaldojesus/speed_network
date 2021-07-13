from django.contrib import admin
from .models import TerminaisOpticos, CaixasDeEmenda, PonPorCaixaEmenda, NumeroPon

# Register your models here.

class TerminaisOpticosAdmin(admin.ModelAdmin):
    list_display = ('id', 'rua_cto','numero_rua_cto','codigo_cto','board_cto', 'pon_cto','conexoes_opticas_cto','quant_conexoes_usadas_cto')
admin.site.register(TerminaisOpticos, TerminaisOpticosAdmin)

class CaxasDeEmendaAdmin(admin.ModelAdmin):
    list_filter = ['codigo_caixa','rua_caixa_emenda','numero_rua_cto']
admin.site.register(CaixasDeEmenda, CaxasDeEmendaAdmin)

admin.site.register(PonPorCaixaEmenda)

admin.site.register(NumeroPon)
