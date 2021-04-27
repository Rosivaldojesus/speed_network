from django.db.models import Sum
from django.shortcuts import render
from .models import Produto
from .models import EntradaProduto, SaidaProduto, TotalProdutos

# Create your views here.
def Index(request):
    produtos = Produto.objects.all()
    return render(request, 'stock/index.html', {'produtos': produtos})

def EntradaProdutos(request):
    entradas = EntradaProduto.objects.all()
    return render(request, 'stock/entrada-produtos.html',{'entradas':entradas})


def SaidaProdutos(request):
    saidas = SaidaProduto.objects.all()
    return render(request, 'stock/saida-produtos.html',{'saidas':saidas} )
