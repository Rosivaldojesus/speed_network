from django.contrib import admin
from .models import PlanosInternet, Cidade, AdicionarQuantidade,\
    DataVencimento, FabricanteEquipamentos, ModelosEquipamentos, Vendedores, Ruas

# Register your models here.
admin.site.register(PlanosInternet)
admin.site.register(Cidade)
admin.site.register(AdicionarQuantidade)
admin.site.register(DataVencimento)
admin.site.register(FabricanteEquipamentos)
admin.site.register(ModelosEquipamentos)
admin.site.register(Vendedores)




class RuasAdmin(admin.ModelAdmin):
    list_display = ('id', 'logradouro', 'bairro', 'cep', 'numero_baixo', 'numero_alto')
    list_filter = ('bairro', 'cep',)
    search_fields = ('id', 'logradouro', 'bairro', 'cep', 'numero_baixo', 'numero_alto')
admin.site.register(Ruas, RuasAdmin)

