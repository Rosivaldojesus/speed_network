from django.contrib import admin
from .models import CategoriaPagamento, Pagamento, TipoCusto, OrigemValores

# Register your models here.

admin.site.register(CategoriaPagamento)
admin.site.register(TipoCusto)
admin.site.register(OrigemValores)


class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('id','motivo_pagamento','valor_pagamento','origem_valor_pagamento','valor_pagamento', 'tipo_custo_pagamento', 'data_pagamento','categoria')
admin.site.register(Pagamento, PagamentoAdmin)
