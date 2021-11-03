from django.contrib import admin
from .models import CategoriaServico, Servico, ServicoVoip, TipoServico


# Register your models here.
admin.site.register(CategoriaServico)

admin.site.register(TipoServico)

class ServicoAdmin(admin.ModelAdmin):
    list_display = ['id','contato_servico', 'data_criacao',
                    'data_agendada','status_agendado',
                    'status_concluido','data_finalizacao',
                    'agendado_por',
                    'criado_por', 'finalizado_por']
    search_fields = ['contato_servico']
admin.site.register(Servico, ServicoAdmin)




class ServicoVoipForm(admin.ModelAdmin):
    list_display = ['nome_usuario_voip','cpf_usuario_voip', 'usuario_voip', 'senha_voip', 'numero_telefone_voip' ]
    search_fields = ['nome_usuario_voip', 'usuario_voip']

admin.site.register(ServicoVoip, ServicoVoipForm)