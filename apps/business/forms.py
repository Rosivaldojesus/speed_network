from django import forms
from . models import VendasProdutos, ComprasProdutos


class VendasProdutosForm(forms.ModelForm):
    class Meta:
        model = VendasProdutos
        fields = ['produto', 'quantidade', 'valor_unitario', 'valor_total', 'observacao']


class EditarVendasProdutosForm(forms.ModelForm):
    class Meta:
        model = VendasProdutos
        fields = ['produto', 'quantidade', 'valor_unitario', 'valor_total', 'observacao']


# Forms para compras
class ComprasProdutosForm(forms.ModelForm):
    class Meta:
        model = ComprasProdutos
        fields = ['produto', 'quantidade', 'valor_unitario', 'valor_total', 'observacao']


class EditarComprasProdutosForm(forms.ModelForm):
    class Meta:
        model = ComprasProdutos
        fields = ['produto', 'quantidade', 'valor_unitario', 'valor_total', 'observacao']
