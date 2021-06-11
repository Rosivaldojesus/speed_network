from django.contrib import admin
from .models import Instalacao


# Register your models here.
class InstalacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cliente','sobrenome_cliente',
                    'data_criacao',
                    'instalacao_vendedor')
    list_filter = ('data_criacao','instalacao_vendedor')



admin.site.register(Instalacao, InstalacaoAdmin)
