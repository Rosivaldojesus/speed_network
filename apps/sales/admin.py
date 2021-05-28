from django.contrib import admin
from .models import Instalacao


# Register your models here.
class InstalacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cliente','status_agendada' ,'boleto_entregue',
                    'data_instalacao','data_finalizacao','concluido','boleto_entregue',
                    'instalacao_criado_por', 'instalacao_finalizado_por')



admin.site.register(Instalacao, InstalacaoAdmin)
