from django.contrib import admin
from .models import Instalacao


# Register your models here.
class InstalacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cliente','status_agendada',
                    'data_criacao',
                    'instalacao_vendedor')
    list_filter = ('status_agendada','instalacao_vendedor')



admin.site.register(Instalacao, InstalacaoAdmin)
