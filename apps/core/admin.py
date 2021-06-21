from django.contrib import admin
from .models import Manuais, SenhasEquipamentos, SenhasPorEquipamentos

# Register your models here.

class ManuaisAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_manual','texto_manual')
admin.site.register(Manuais, ManuaisAdmin)


class SenhasEquipamentosAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip_equipamento','fabricante','equipamento', 'login', 'senha')
    list_editable = ('login', 'senha')
admin.site.register(SenhasEquipamentos, SenhasEquipamentosAdmin)


class SenhasPorEquipamentosAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo_equipamento','sn_equipamento', 'equipamento', 'ip_equipamento','login','senha', 'patrimonio_equipamento' )
    list_display_links = ('id','codigo_equipamento','sn_equipamento')
    search_fields = ('codigo_equipamento',)
    list_filter = ('codigo_equipamento',)
admin.site.register(SenhasPorEquipamentos,SenhasPorEquipamentosAdmin)


