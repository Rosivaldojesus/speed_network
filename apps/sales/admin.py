from django.contrib import admin
from .models import Instalacao


# Register your models here.
class InstalacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cliente','status_agendada' ,'boleto_entregue','data_instalacao','concluido')
    list_editable = ('nome_cliente','status_agendada' , 'boleto_entregue','data_instalacao','concluido')


admin.site.register(Instalacao, InstalacaoAdmin)
