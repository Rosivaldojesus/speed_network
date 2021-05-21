from django import forms
from .models import Pagamento

class CadastarPagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields =['motivo_pagamento',
                 'valor_pagamento',
                 'origem_valor_pagamento',
                 'tipo_custo_pagamento',
                 'data_pagamento',
                 'categoria',
                 ]

    data_pagamento = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))