from django.contrib import admin
from .models import PlanosInternet, Cidade, AdicionarQuantidade,\
    DataVencimento, FabricanteEquipamentos, ModelosEquipamentos, Vendedores

# Register your models here.
admin.site.register(PlanosInternet)
admin.site.register(Cidade)
admin.site.register(AdicionarQuantidade)
admin.site.register(DataVencimento)
admin.site.register(FabricanteEquipamentos)
admin.site.register(ModelosEquipamentos)
admin.site.register(Vendedores)

