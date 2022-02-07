from django.db.models import Q
from django.shortcuts import render
from .models import Produto
from .models import EntradaProduto, SaidaProduto

# Create your views here.


def Index(request):
    produtos = Produto.objects.all()
    queryset = request.GET.get('q')
    if queryset:
        produtos = Produto.objects.filter(
            Q(nome_produto__icontains=queryset) |
            Q(marca_produto__icontains=queryset) |
            Q(modelo_produto__icontains=queryset))
    context = {
        'produtos': produtos
    }
    return render(request, 'stock/index.html', context)


def EntradaProdutos(request):
    entradas = EntradaProduto.objects.all()
    context = {
        'entradas': entradas
    }
    return render(request, 'stock/entrada-produtos.html', context)


def SaidaProdutos(request):
    saidas = SaidaProduto.objects.all()
    context = {
        'saidas': saidas
    }
    return render(request, 'stock/saida-produtos.html', context)
