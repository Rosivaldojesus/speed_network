from django.contrib import admin
from .models import CategoriaPagamento, Pagamento, TipoCusto, OrigemValores
from .models import AgendaPagamento, FluxoEntradasSaidas

# Register your models here.

admin.site.register(CategoriaPagamento)
admin.site.register(TipoCusto)
admin.site.register(OrigemValores)


class AgendaPagamentoForm(admin.ModelAdmin):
    list_display = ('id', 'motivo_pagamento','valor_pagamento' ,'categoria', 'data_pagamento', 'status_pago')
    list_editable = ('motivo_pagamento','valor_pagamento' ,'categoria', 'data_pagamento', 'status_pago')

admin.site.register(AgendaPagamento, AgendaPagamentoForm)

class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'motivo_pagamento',
                    'valor_pagamento',
                    'origem_valor_pagamento',
                    'tipo_custo_pagamento',
                    'data_pagamento',
                    'categoria',
                    'status_pago',

                    )
    list_filter = [
                    'origem_valor_pagamento',
                    'tipo_custo_pagamento',
                    'data_pagamento',
                    'categoria']
    list_display_links = ['motivo_pagamento']
    search_fields = ['motivo_pagamento',
                    'valor_pagamento',
                    ]
admin.site.register(Pagamento, PagamentoAdmin)

admin.site.register(FluxoEntradasSaidas)
