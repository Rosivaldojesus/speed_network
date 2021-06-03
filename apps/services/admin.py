from django.contrib import admin
from .models import CategoriaServico, Servico, ServicoVoip

# Register your models here.
admin.site.register(CategoriaServico)

class ServicoAdmin(admin.ModelAdmin):
    list_display = ['id','categoria', 'data_criacao',
                    'data_agendada','status_agendado',
                    'status_concluido','data_finalizacao',
                    'agendado_por',
                    'criado_por', 'finalizado_por']
admin.site.register(Servico, ServicoAdmin)

class ServicoVoipForm(admin.ModelAdmin):
    list_display = ['nome_usuario_voip', 'usuario_voip', 'senha_voip', 'numero_telefone_voip' ]

admin.site.register(ServicoVoip, ServicoVoipForm)