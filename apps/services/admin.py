from django.contrib import admin
from .models import CategoriaServico, Servico

# Register your models here.




admin.site.register(CategoriaServico)


class ServicoAdmin(admin.ModelAdmin):
    list_display = ['id','categoria', 'data_criacao',
                    'data_agendada','status_agendado',
                    'status_concluido','data_finalizacao',
                    'criado_por', 'finalizado_por']


admin.site.register(Servico, ServicoAdmin)