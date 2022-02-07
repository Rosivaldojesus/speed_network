from django import forms
from .models import SenhasPorEquipamentos


class SenhasPorEquipamentosForm(forms.ModelForm):
    class Meta:
        model = SenhasPorEquipamentos
        fields = [
            'codigo_equipamento',
            'sn_equipamento',
            'equipamento',
            'ip_equipamento',
            'login',
            'senha',
            'fabricante',
            'patrimonio_equipamento'
        ]
