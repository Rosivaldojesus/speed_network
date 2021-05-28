from django import forms
from .models import Pagamento, AgendaPagamento

class CadastarPagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields =['motivo_pagamento',
                 'valor_pagamento',
                 'origem_valor_pagamento',
                 'tipo_custo_pagamento',
                 'data_pagamento',
                 'categoria',
                 'status_pago',
                 ]
    data_pagamento = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    status_pago = forms.BooleanField(required=True, initial=True, label='Comfirmar pagamento')


class AgendarPagamentoForm(forms.ModelForm):
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



'''
class AgendarPagamentoForm(forms.ModelForm):
    class Meta:
        model = AgendaPagamento
        fields = ['data_pagamento',]
    data_pagamento = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
'''

class ComfirmarPagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['status_pago']

    status_pago = forms.BooleanField(required=True, initial=False, label='Comfirmar pagamento')
