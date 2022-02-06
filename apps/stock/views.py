from django.db.models import Sum, Q
from django.shortcuts import render
from .models import Produto
from .models import EntradaProduto, SaidaProduto, TotalProdutos

# Create your views here.
def Index(request):
    produtos = Produto.objects.all()
    queryset = request.GET.get('q')
    if queryset:
        produtos = Produto.objects.filter(
            Q(nome_produto__icontains=queryset) |
            Q(marca_produto__icontains=queryset)|
            Q(modelo_produto__icontains=queryset))
    return render(request, 'stock/indexxx.html', {'produtos': produtos})

def EntradaProdutos(request):
    entradas = EntradaProduto.objects.all()
    return render(request, 'stock/entrada-produtos.html',{'entradas':entradas})


def SaidaProdutos(request):
    saidas = SaidaProduto.objects.all()
    return render(request, 'stock/saida-produtos.html',{'saidas':saidas} )