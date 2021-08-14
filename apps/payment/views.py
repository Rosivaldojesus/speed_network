from datetime import date, datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Sum, Count
from .models import Pagamento, AgendaPagamento
from .forms import CadastarPagamentoForm, AgendarPagamentoForm, ComfirmarPagamentoForm, EditarPagamentoForm
from django.contrib import messages
from django.db.models.functions import ExtractMonth
from django.db.models.functions import TruncMonth
import csv
from django.http import HttpResponse

# Create your views here.
def Index(request):
    data_atual = datetime.now()
    this_month = date.today().month
    dia = Pagamento.objects.values('data_pagamento').annotate(number=Sum('valor_pagamento')).order_by('-data_pagamento')
    mes = Pagamento.objects.annotate(month=ExtractMonth('data_pagamento')).values('month').annotate(count=Sum('valor_pagamento'))

    #Query para o total de gatos de cada mês
    mes =  Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(data_pagamento__lt=data_atual).filter().values('month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')

    pagamentos = Pagamento.objects.all().order_by('-data_pagamento')

    #Contagem de gastos mensais por catergoria!!!
    veiculos = Pagamento.objects.filter(categoria=1).aggregate(total=Sum('valor_pagamento'))
    funcionarios = Pagamento.objects.filter(categoria=2).aggregate(total=Sum('valor_pagamento'))
    alimentacao = Pagamento.objects.filter(categoria=3).aggregate(total=Sum('valor_pagamento'))
    links = Pagamento.objects.filter(categoria=4).aggregate(total=Sum('valor_pagamento'))
    locacao = Pagamento.objects.filter(categoria=5).aggregate(total=Sum('valor_pagamento'))
    instalacao = Pagamento.objects.filter(categoria=6).aggregate(total=Sum('valor_pagamento'))
    socios = Pagamento.objects.filter(categoria=7).aggregate(total=Sum('valor_pagamento'))

    veiculosMesAtual = Pagamento.objects.filter(data_pagamento__month=this_month).filter(categoria=1).aggregate(total=Sum('valor_pagamento'))
    funcionariosMesAtual = Pagamento.objects.filter(data_pagamento__month=this_month).filter(categoria=2).aggregate(total=Sum('valor_pagamento'))
    alimentacaoMesAtual = Pagamento.objects.filter(data_pagamento__month=this_month).filter(categoria=3).aggregate(total=Sum('valor_pagamento'))
    linksMesAtual = Pagamento.objects.filter(data_pagamento__month=this_month).filter(categoria=4).aggregate(total=Sum('valor_pagamento'))
    locacaoMesAtual = Pagamento.objects.filter(data_pagamento__month=this_month).filter(categoria=5).aggregate(total=Sum('valor_pagamento'))
    instalacaoMesAtual = Pagamento.objects.filter(data_pagamento__month=this_month).filter(categoria=6).aggregate(total=Sum('valor_pagamento'))
    sociosMesAtual = Pagamento.objects.filter(data_pagamento__month=this_month).filter(categoria=7).aggregate(total=Sum('valor_pagamento'))
    ImpostosMesAtual = Pagamento.objects.filter(data_pagamento__month=this_month).filter(categoria=8).aggregate(total=Sum('valor_pagamento'))


    #Query para total por mês de custo das categorias
    mensalVeiculos = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(categoria=1).values('month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    mensalFuncionarios = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(categoria=2).values('month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    mensalAlimentacao = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter().filter(categoria=3).values('month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    mensalLinks = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(categoria=4).values('month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    mensalLocacao = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(data_pagamento__lt=data_atual).filter(categoria=5).values('month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    mensalInstalacao = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(categoria=6).values('month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    mensalSocios = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(categoria=7).values('month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    mensalImpostos = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(categoria=8).values('month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')

    #Query para o mês atual das categorias de custos
    atualMensalVeiculos = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(data_pagamento__month=this_month).filter(categoria=1).values('month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    atualMensalFuncionarios = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(data_pagamento__month=this_month).filter(categoria=2).values('month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    atualMensalAlimentacao = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(data_pagamento__month=this_month).filter(categoria=3).values('month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    atualMensalLinks = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(data_pagamento__month=this_month).filter(categoria=4).values('month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    atualMensalLocacao = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(data_pagamento__month=this_month).filter(categoria=5).values('month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    atualmensalInstalacao = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(data_pagamento__month=this_month).filter(categoria=6).values('month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    atualMensalSocios = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(data_pagamento__month=this_month).filter(categoria=7).values('month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')


    return render(request, 'payment/index.html', {'pagamentos':pagamentos, 'dia': dia,'mes': mes,
                                                  'veiculos':veiculos,
                                                  'funcionarios':funcionarios,
                                                  'alimentacao': alimentacao,
                                                  'links': links,
                                                  'locacao': locacao,
                                                  'instalacao': instalacao,
                                                  'socios': socios,

                                                  'atualMensalVeiculos':atualMensalVeiculos,
                                                  'atualMensalFuncionarios':atualMensalFuncionarios,
                                                  'atualMensalAlimentacao': atualMensalAlimentacao,
                                                  'atualMensalLinks':atualMensalLinks,
                                                  'atualMensalLocacao':atualMensalLocacao,
                                                  'atualmensalInstalacao':atualmensalInstalacao,
                                                  'atualMensalSocios':atualMensalSocios,

                                                  'veiculosMesAtual':veiculosMesAtual,
                                                  'funcionariosMesAtual':funcionariosMesAtual,
                                                  'alimentacaoMesAtual':alimentacaoMesAtual,
                                                  'linksMesAtual':linksMesAtual,
                                                  'locacaoMesAtual':locacaoMesAtual,
                                                  'instalacaoMesAtual':instalacaoMesAtual,
                                                  'sociosMesAtual':sociosMesAtual,
                                                  'ImpostosMesAtual':ImpostosMesAtual,


                                                  'mensalVeiculos':mensalVeiculos,
                                                  'mensalFuncionarios':mensalFuncionarios,
                                                  'mensalAlimentacao':mensalAlimentacao,
                                                  'mensalLinks':mensalLinks,
                                                  'mensalLocacao':mensalLocacao,
                                                  'mensalInstalacao':mensalInstalacao,
                                                  'mensalSocios':mensalSocios,
                                                  'mensalImpostos':mensalImpostos,


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
    pagamentos = Pagamento.objects.all().order_by('-data_pagamento')

    queryset = request.GET.get('q')
    motivoPagamento = request.GET.get('motivoPagamento')
    if queryset:
        pagamentos = Pagamento.objects.filter(Q(data_pagamento__icontains=queryset))
    elif motivoPagamento:
        pagamentos = Pagamento.objects.filter(Q(motivo_pagamento__icontains=motivoPagamento))



        dia = Pagamento.objects.values('data_pagamento').annotate(
            number=Sum('valor_pagamento'))
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

def PagamentosFuturos(request):
    data_atual = datetime.now()
    naoVencidas = Pagamento.objects.filter(status_pago='False').filter(data_pagamento__gt=data_atual)
    return render(request, 'payment/pagamentos-futuros.html',{'naoVencidas':naoVencidas})


from django.http import JsonResponse

"""
   for entry in mensalVeiculos:
        labels.append(entry['month'])
        data.append(entry['c'])
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
"""
def PagamentosMensaisGrupos(request):
    data_atual = datetime.now()

    labels = []
    data = []

    mensalVeiculos = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(categoria=1).values(
        'month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    for entry in mensalVeiculos:


        labels.append(entry['month'])
        data.append(entry['c'])


    mensalFuncionarios = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(categoria=2).values(
        'month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    mensalAlimentacao = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter().filter(
        categoria=3).values('month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    mensalLinks = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(categoria=4).values(
        'month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    mensalLocacao = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(
        data_pagamento__lt=data_atual).filter(categoria=5).values('month').annotate(c=Sum('valor_pagamento')).values(
        'month', 'c').order_by('month')
    mensalInstalacao = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(categoria=6).values(
        'month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    mensalSocios = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(categoria=7).values(
        'month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    mensalImpostos = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(categoria=8).values(
        'month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')

    return render(request, 'payment/pagamentos-mensais-grupos.html', {
        'data': data,
        'labels': labels,
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



#Exportando os dados para CSV
def ExportarCSV(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="relatorio-pagamentos.csv"'

    pagamentos = Pagamento.objects.all()

    writer = csv.writer(response)
    writer.writerow(['id', 'data_pagamento', 'motivo_pagamento', 'valor_pagamento', 'origem_valor_pagamento',
                     'tipo_custo_pagamento', 'categoria', 'status_pago'])
    for pag in pagamentos:
        writer.writerow([pag.id, pag.data_pagamento, pag.motivo_pagamento, pag.valor_pagamento,
                         pag.origem_valor_pagamento, pag.tipo_custo_pagamento,  pag.categoria , pag.status_pago
                         ])
    return response