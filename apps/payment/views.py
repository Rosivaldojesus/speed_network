from datetime import date

from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Pagamento
from .forms import CadastarPagamentoForm
from django.contrib import messages
from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth
from django.db.models.functions import ExtractMonth

# Create your views here.
def Index(request):

    dia = Pagamento.objects.filter().values('data_pagamento').annotate(number=Sum('valor_pagamento')).order_by('-data_pagamento')

    mes = Pagamento.objects.annotate(month=ExtractMonth('data_pagamento')).values('month').annotate(count=Sum('valor_pagamento')).values('month','count')
    pagamentos = Pagamento.objects.all()
    return render(request, 'payment/index.html', {'pagamentos':pagamentos,
                                                'dia': dia,
                                                  'mes': mes,
                                                })

def CadastrarPagamento(request):
    form = CadastarPagamentoForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Pagamento adicionado com sucesso!')
        return redirect('/pagamentos/')
    else:
        form = CadastarPagamentoForm()
    return render(request, 'payment/cadastrar-pagamento.html',{'form': form})

def DashboardPagamentos(request):
    return render(request, 'payment/dashboard-pagamentos.html')

def TodosPagamentos(request):
    pagamentos = Pagamento.objects.all()

    inicial = date(2021, 5, 20)
    final = date(2021, 5, 22)


    pagamentos = Pagamento.objects.filter(data_pagamento__range=[inicial, final])



    return render(request, 'payment/todos_pagamentos.html', {'pagamentos': pagamentos})