from django.contrib import admin
from .models import PlanosInternet, Cidade, AdicionarQuantidade, DataVencimento, FabricanteEquipamentos, Bancos, Ruas, \
    ModelosEquipamentos, Vendedores, FuncionariosParaVale, Bairros

# Register your models here.


admin.site.register(PlanosInternet)
admin.site.register(Cidade)
admin.site.register(AdicionarQuantidade)
admin.site.register(DataVencimento)
admin.site.register(FabricanteEquipamentos)
admin.site.register(ModelosEquipamentos)
admin.site.register(Vendedores)
admin.site.register(FuncionariosParaVale)
admin.site.register(Bairros)
admin.site.register(Bancos)


class RuasAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'logradouro', 'bairro_ruas','bairro' ,'cep'
    )
    list_filter = (
        'bairro_ruas', 'cep',
    )
    search_fields = (
        'id', 'logradouro', 'bairro_ruas', 'cep', 
    )
    list_editable = ('logradouro', 'bairro_ruas')


admin.site.register(Ruas, RuasAdmin)
