from django import forms
from .models import Pagamento

class CadastarPagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields =['motivo_pagamento',

                 ]

