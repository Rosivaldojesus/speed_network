from datetime import date, datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Pagamento, AgendaPagamento
from .forms import CadastarPagamentoForm, AgendarPagamentoForm, ComfirmarPagamentoForm, EditarPagamentoForm
from django.contrib import messages
from django.db.models import Count, Sum
from django.db.models.functions import ExtractMonth

# Create your views here.
def Index(request):
    dia = Pagamento.objects.values('data_pagamento').annotate(
        number=Sum('valor_pagamento')).order_by('-data_pagamento')
    mes = Pagamento.objects.annotate(month=ExtractMonth('data_pagamento')).values(
        'month').annotate(count=Sum('valor_pagamento'))
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


def ListaPagamentos(request):
    inicial = date(2021, 5, 20)
    final = date(2021, 5, 22)
    pagamentos = Pagamento.objects.filter(data_pagamento__range=[inicial, final])
    pagamentos = Pagamento.objects.all()
    queryset = request.GET.get('q')
    if queryset:
        pagamentos = Pagamento.objects.filter(
            Q(data_pagamento__icontains=queryset))
    return render(request, 'payment/lista_pagamentos.html', {'pagamentos': pagamentos})


def AgendamentosPagamentos(request):
    data_atual = datetime.now()
    vencerHoje = Pagamento.objects.filter(status_pago= 'False').filter(data_pagamento = data_atual)
    atrasadas = Pagamento.objects.filter(status_pago= 'False').filter(data_pagamento__lt=data_atual)
    naoVencidas = Pagamento. objects.filter(status_pago= 'False').filter(data_pagamento__gt=data_atual)
    totalPagarHoje = Pagamento.objects.filter(status_pago= 'False').filter(data_pagamento=data_atual)\
        .aggregate(total=Sum('valor_pagamento'))
    totalPagarAtrasadas = Pagamento.objects.filter(status_pago= 'False').filter(data_pagamento__lt=data_atual)\
        .aggregate(total=Sum('valor_pagamento'))
    totalPagarNaoVencidas = Pagamento.objects.filter(status_pago= 'False').filter(data_pagamento__gt=data_atual)\
        .aggregate(total=Sum('valor_pagamento'))
    return render(request, 'payment/agendamentos-pagamentos.html', { 'vencerHoje': vencerHoje,
                                                                     'atrasadas': atrasadas,
                                                                     'naoVencidas': naoVencidas,
                                                                     'totalPagarHoje': totalPagarHoje,
                                                                     'totalPagarAtrasadas': totalPagarAtrasadas,
                                                                     'totalPagarNaoVencidas': totalPagarNaoVencidas,
                                                                     })


def AgendarPagamento(request):
    form = AgendarPagamentoForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Pagamento agendado com sucesso!')
        return redirect('/pagamentos/')
    else:
        form = AgendarPagamentoForm()
    return render(request, 'payment/agendar-pagamento.html',{'form': form})


def EditarPagamento(request, id=None):
    pagar = get_object_or_404(Pagamento, id=id)
    form = EditarPagamentoForm(request.POST or None, instance=pagar)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Pagamento alterado com sucesso.')
        return redirect('/pagamentos/')
    return render(request, 'payment/editar-pagamento.html', {'form': form})


def ConfirmarPagamento(request, id=None):
    pagar = get_object_or_404(Pagamento, id=id)
    form = ComfirmarPagamentoForm(request.POST or None, instance=pagar)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Pagamento comfirmado com sucesso.')
        return redirect('/pagamentos/')
    return render(request, 'payment/comfirmar-pagamento.html', {'form': form})