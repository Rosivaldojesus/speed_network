from django.contrib import admin
from .models import ServicoVoip

# Register your models here.
class ServicoVoipAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'nome_usuario_voip',
                    'cpf_usuario_voip',
                    'usuario_voip',
                    'senha_voip',
                    'numero_telefone_voip',
                    'data_reserva_voip',
                    'portabilidade_voip',
                    'finalizado_voip',
                    'funcionario_reserva_voip',
                    'reservado_voip',
                    'boleto_entregue',
                    ]
    search_fields = ['nome_usuario_voip', 'usuario_voip']
admin.site.register(ServicoVoip, ServicoVoipAdmin)

