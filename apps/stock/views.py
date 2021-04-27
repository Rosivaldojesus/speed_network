from django.db.models import Sum
from django.shortcuts import render
from .models import Produto
from .models import EntradaProduto, SaidaProduto

# Create your views here.
def Index(request):
    produtos = Produto.objects.all()


    return render(request, 'stock/index.html', {'produtos': produtos,

                                                })