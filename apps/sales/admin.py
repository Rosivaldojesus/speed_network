from django.contrib import admin
from .models import Instalacao, ClientesVoip, ValeRefeicao, Cancelamentos


# Register your models here.
class InstalacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cliente','sobrenome_cliente',
                    'data_finalizacao',
                    'instalacao_vendedor')
    list_filter = ('data_criacao','instalacao_vendedor')
    search_fields = ('nome_cliente', 'sobrenome_cliente')
admin.site.register(Instalacao, InstalacaoAdmin)

admin.site.register(ClientesVoip)



class ValeRefeicaoAdmin(admin.ModelAdmin):
    list_display = ('id','nome_funcionario','data_criacao','data_vale','valor_vale','status_pago')
admin.site.register(ValeRefeicao, ValeRefeicaoAdmin)



class CancelamentosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'plano_internet','data_criacao','atendente')
admin.site.register(Cancelamentos, CancelamentosAdmin)