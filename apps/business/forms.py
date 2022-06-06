from django import forms
from . models import VendasProdutos


class VendasProdutosForm(forms.ModelForm):

    class Meta:
        model = VendasProdutos
        fields = ['produto', 'quantidade', 'valor_unitario', 'valor_total', 'observacao']


class EditarVendasProdutosForm(forms.ModelForm):
    
    class Meta:
        model = VendasProdutos
        fields = ['produto', 'quantidade', 'valor_unitario', 'valor_total', 'observacao']

