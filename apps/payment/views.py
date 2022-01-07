from datetime import date, datetime
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Sum, Avg, F
from django.views.generic import CreateView, UpdateView
from django.views.generic.list import ListView
from .forms import CadastarDestinoValoresBoletosForm, EditarDestinoValoresBoletosForm
from .models import Pagamento, FluxoEntradasSaidas, DestinoValoresBoletos, ClientesEntregaBoletos
from .forms import CadastarPagamentoForm, AgendarPagamentoForm, ComfirmarPagamentoForm, EditarPagamentoForm, \
    ClientesEntregaBoletosForm, EditarClientesEntregaBoletosForm, CadastrarFluxoForm
from django.contrib import messages
from django.db.models.functions import TruncMonth
import csv
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from dateutil.relativedelta import relativedelta
from .models import FluxoEntradaSaidaMensal


# Create your views here.


class IndexTemplateView(TemplateView):
    model = Pagamento
    template_name = 'payment/indexx.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_month = date.today().month  # Variável do mês atual
        data_atual = datetime.now()  # Variável da data de hoje
        data_inicial = '2021-6-1'
        six_months = date.today() + relativedelta(months=-5)


        # Query para o total de gastos de cada mês =====================================================================
        context['mes'] = Pagamento.objects.\
            annotate(month=TruncMonth('data_pagamento'), c=Sum('valor_pagamento')). \
            values('month').\
            annotate(c=Sum('valor_pagamento')).\
            filter(data_pagamento__lte=data_atual).\
            filter().values(
            'month', 'c').\
            order_by('month')

        # Query [Gráfico] para total por mês de custo das categorias ===================================================
        context['mensais_categoria'] = Pagamento.objects. \
            filter(status_pago=True). \
            filter(Q(data_pagamento__range=[data_inicial, data_atual])). \
            annotate(month=TruncMonth('data_pagamento')). \
            values('month'). \
            annotate(total=Sum('valor_pagamento')). \
            values('month', 'total', 'categoria'). \
            order_by('month')

        # Query de mês atual dos gastos por categoria ==================================================================
        context['veiculosMesAtual'] = Pagamento.objects.filter(data_pagamento__month=this_month) \
            .filter(status_pago=True).filter(categoria=1).aggregate(total=Sum('valor_pagamento'))
        context['funcionariosMesAtual'] = Pagamento.objects.filter(data_pagamento__month=this_month) \
            .filter(status_pago=True).filter(categoria=2).aggregate(total=Sum('valor_pagamento'))
        context['alimentacaoMesAtual'] = Pagamento.objects.filter(data_pagamento__month=this_month) \
            .filter(status_pago=True).filter(categoria=3).aggregate(total=Sum('valor_pagamento'))
        context['linksMesAtual'] = Pagamento.objects.filter(data_pagamento__month=this_month) \
            .filter(status_pago=True).filter(categoria=4).aggregate(total=Sum('valor_pagamento'))
        context['locacaoMesAtual'] = Pagamento.objects.filter(data_pagamento__month=this_month) \
            .filter(status_pago=True).filter(categoria=5).aggregate(total=Sum('valor_pagamento'))
        context['instalacaoMesAtual'] = Pagamento.objects.filter(data_pagamento__month=this_month).filter(
            status_pago=True).filter(categoria=6).aggregate(total=Sum('valor_pagamento'))
        context['sociosMesAtual'] = Pagamento.objects.filter(data_pagamento__month=this_month).filter(
            status_pago=True).filter(categoria=7).aggregate(total=Sum('valor_pagamento'))
        context['ImpostosMesAtual'] = Pagamento.objects.filter(data_pagamento__month=this_month).filter(
            status_pago=True).filter(categoria=8).aggregate(total=Sum('valor_pagamento'))
        context['taxaMesAtual'] = Pagamento.objects.filter(data_pagamento__month=this_month).filter(
            status_pago=True).filter(categoria=11).aggregate(total=Sum('valor_pagamento'))

        return context


class CustoMensalCategoriaView(TemplateView):
    model = Pagamento
    template_name = 'payment/custo-mensal-categoria.html'

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        six_months = date.today() + relativedelta(months=-6)
        last_months = date.today() + relativedelta(months=-0)

        # Query para total por mês de custo das categorias
        context['custos_mensais_categoria'] = Pagamento.objects. \
            filter(status_pago=True). \
            filter(Q(data_pagamento__range=[six_months, last_months])). \
            annotate(media_total=Sum('valor_pagamento')).\
            annotate(month=TruncMonth('data_pagamento')).  \
            values('month'). \
            annotate(total=Sum('valor_pagamento')). \
            values('month', 'total', 'categoria'). \
            order_by('month')[1:]

        context['media_veiculos'] = Pagamento.objects.filter(categoria=1).\
            filter(Q(data_pagamento__range=[six_months, last_months])).aggregate(total=Sum('valor_pagamento') / 6)
        context['media_funcionarios'] = Pagamento.objects.filter(categoria=2). \
            filter(Q(data_pagamento__range=[six_months, last_months])).aggregate(total=Sum('valor_pagamento') / 6)
        context['media_alimentacao'] = Pagamento.objects.filter(categoria=3). \
            filter(Q(data_pagamento__range=[six_months, last_months])).aggregate(total=Sum('valor_pagamento') / 6)
        context['media_links'] = Pagamento.objects.filter(categoria=4). \
            filter(Q(data_pagamento__range=[six_months, last_months])).aggregate(total=Sum('valor_pagamento') / 6)
        context['media_locacao'] = Pagamento.objects.filter(categoria=5). \
            filter(Q(data_pagamento__range=[six_months, last_months])).aggregate(total=Sum('valor_pagamento') / 6)
        context['media_instalacao'] = Pagamento.objects.filter(categoria=6). \
            filter(Q(data_pagamento__range=[six_months, last_months])).aggregate(total=Sum('valor_pagamento') / 6)
        context['media_socios'] = Pagamento.objects.filter(categoria=7). \
            filter(Q(data_pagamento__range=[six_months, last_months])).aggregate(total=Sum('valor_pagamento') / 6)
        context['media_impostos'] = Pagamento.objects.filter(categoria=8). \
            filter(Q(data_pagamento__range=[six_months, last_months])).aggregate(total=Sum('valor_pagamento') / 6)
        context['media_taxas'] = Pagamento.objects.filter(categoria=11). \
            filter(Q(data_pagamento__range=[six_months, last_months])).aggregate(total=Sum('valor_pagamento') / 6)

        return context


class FluxoEntradaSaidaView(TemplateView):
    model = FluxoEntradaSaidaMensal, Pagamento
    template_name = 'payment/fluxo-entrada-saida.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['entrada_banco'] = FluxoEntradaSaidaMensal.objects.\
            annotate(month=TruncMonth('data_registro')) \
            .values('month').\
            annotate(c=Sum('entrada_mes_atual')).\
            values('month', 'c').\
            order_by('month')

        context['entrada_erp'] = FluxoEntradaSaidaMensal.objects.\
            annotate(month=TruncMonth('data_registro')) \
            .values('month').\
            annotate(c=Sum('entrada_referente_mes_atual')).\
            values('month', 'c').\
            order_by('month')

        context['custos_gerais'] = FluxoEntradaSaidaMensal.objects. \
            annotate(month=TruncMonth('data_registro')) \
            .values('month'). \
            annotate(c=Sum('entrada_referente_mes_atual')). \
            values('month', 'c'). \
            order_by('month')

        return context


class ContarPagarView(TemplateView):
    model = Pagamento
    template_name = 'payment/contas-a-pagar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_day = date.today()  # Variável do mês atual

        context['valor_a_pagar'] = Pagamento.objects.filter(status_pago=False).filter(data_pagamento__gt=this_day).\
            aggregate(total=Sum('valor_pagamento'))

        context['valor_a_pagar_hoje'] = Pagamento.objects.filter(data_pagamento=this_day).filter(status_pago=False). \
            aggregate(total=Sum('valor_pagamento'))

        context['valor_a_pagar_atrasada'] = Pagamento.objects.filter(data_pagamento__lt=this_day).\
            filter(status_pago=False).aggregate(total=Sum('valor_pagamento'))

        context['lista_conta_a_hoje'] = Pagamento.objects.filter(status_pago='False').filter(data_pagamento=this_day)
        context['lista_conta_atrasadas'] = Pagamento.objects.filter(status_pago='False').filter(data_pagamento__lt=this_day)

        context['pagamentos_futuros_mensal'] = Pagamento.objects.filter(status_pago='False').annotate(
            month=TruncMonth('data_pagamento')).filter(
            data_pagamento__gt=this_day).values('month').annotate(
            c=Sum('valor_pagamento')).values('month', 'c').order_by('month')



        return context


class ContasVencerView(TemplateView):
    model = Pagamento
    template_name = 'payment/contas-a-vencer.html'

    def get_context_data(self, **kwargs):
        context = super(ContasVencerView, self).get_context_data()

        motivo_pagamento = self.request.GET.get('motivo_pagamento')
        valor = self.request.GET.get('valor')
        data = self.request.GET.get('data')

        context['valor_a_pagar'] = Pagamento.objects.filter(status_pago=False).\
            aggregate(total=Sum('valor_pagamento'))

        if motivo_pagamento:
            context['conta_a_vencer'] = Pagamento.objects.filter(status_pago=False).\
                filter(Q(motivo_pagamento__icontains=motivo_pagamento)).order_by('data_pagamento')
        elif data:
            context['conta_a_vencer'] = Pagamento.objects.filter(status_pago=False).\
                filter(Q(data_pagamento__exact=data)).order_by('data_pagamento')
        elif valor:
            context['conta_a_vencer'] = Pagamento.objects.filter(status_pago=False).\
                filter(Q(valor_pagamento__exact=valor)).order_by('data_pagamento')
        else:
            context['conta_a_vencer'] = Pagamento.objects.filter(status_pago=False).order_by('data_pagamento')

        return context





class EditarPagamentoAgendadoView(UpdateView):
    model = Pagamento
    fields = '__all__'
    template_name = 'payment/atualizar-pagamento.html'
    success_url = '/pagamentos/contas-a-pagar/'

#  =======================================================================================================================
#  =======================================================================================================================
#  =======================================================================================================================


def Index(request):
    data_atual = datetime.now()
    this_month = date.today().month
    dia = Pagamento.objects.values('data_pagamento').annotate(number=Sum('valor_pagamento')).order_by('-data_pagamento')

    # Query para o total de gastos de cada mês
    mes = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(
        data_pagamento__lte=data_atual).filter(status_pago=True).values('month').annotate(c=Sum(
            'valor_pagamento')).values('month', 'c').order_by('month')
    custo_mes = Pagamento.objects.annotate(month=TruncMonth('data_pagamento'), c=Sum('valor_pagamento')).values(
        'month').annotate(c=Sum('valor_pagamento')).filter(data_pagamento__lte=data_atual).filter().values(
        'month', 'c').order_by('month')

    pagamentos = Pagamento.objects.all().order_by('-data_pagamento')

    # Contagem de gastos mensais por catergoria!!!
    veiculos = Pagamento.objects.filter(categoria=1).aggregate(total=Sum('valor_pagamento'))
    funcionarios = Pagamento.objects.filter(categoria=2).aggregate(total=Sum('valor_pagamento'))
    alimentacao = Pagamento.objects.filter(categoria=3).aggregate(total=Sum('valor_pagamento'))
    links = Pagamento.objects.filter(categoria=4).aggregate(total=Sum('valor_pagamento'))
    locacao = Pagamento.objects.filter(categoria=5).aggregate(total=Sum('valor_pagamento'))
    instalacao = Pagamento.objects.filter(categoria=6).aggregate(total=Sum('valor_pagamento'))
    socios = Pagamento.objects.filter(categoria=7).aggregate(total=Sum('valor_pagamento'))

    # Query de mês atual dos gastos por categoria
    veiculosMesAtual = Pagamento.objects.filter(data_pagamento__month=this_month).filter(status_pago=True) \
        .filter(categoria=1).aggregate(total=Sum('valor_pagamento'))
    funcionariosMesAtual = Pagamento.objects.filter(data_pagamento__month=this_month).filter(status_pago=True).filter(
        categoria=2).aggregate(total=Sum('valor_pagamento'))
    alimentacaoMesAtual = Pagamento.objects.filter(data_pagamento__month=this_month).filter(status_pago=True).filter(
        categoria=3).aggregate(total=Sum('valor_pagamento'))
    linksMesAtual = Pagamento.objects.filter(data_pagamento__month=this_month).filter(status_pago=True).filter(
        categoria=4).aggregate(total=Sum('valor_pagamento'))
    locacaoMesAtual = Pagamento.objects.filter(data_pagamento__month=this_month).filter(status_pago=True).filter(
        categoria=5).aggregate(total=Sum('valor_pagamento'))
    instalacaoMesAtual = Pagamento.objects.filter(data_pagamento__month=this_month).filter(status_pago=True).filter(
        categoria=6).aggregate(total=Sum('valor_pagamento'))
    sociosMesAtual = Pagamento.objects.filter(data_pagamento__month=this_month).filter(status_pago=True).filter(
        categoria=7).aggregate(total=Sum('valor_pagamento'))
    ImpostosMesAtual = Pagamento.objects.filter(data_pagamento__month=this_month).filter(status_pago=True).filter(
        categoria=8).aggregate(total=Sum('valor_pagamento'))
    taxaMesAtual = Pagamento.objects.filter(data_pagamento__month=this_month).filter(status_pago=True).filter(
        categoria=11).aggregate(total=Sum('valor_pagamento'))

    # Query para total por mês de custo das categorias
    mensalVeiculos = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(
        data_pagamento__lte=data_atual).filter(categoria=1).values('month').annotate(c=Sum('valor_pagamento')).values(
        'month', 'c').order_by('-month')
    mensalFuncionarios = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(
        data_pagamento__lte=data_atual).filter(categoria=2).values('month').annotate(c=Sum('valor_pagamento')).values(
        'month', 'c').order_by('-month')
    mensalAlimentacao = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(
        data_pagamento__lte=data_atual).filter().filter(categoria=3).values('month').annotate(
        c=Sum('valor_pagamento')).values('month', 'c').order_by('-month')
    mensalLinks = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(
        data_pagamento__lte=data_atual).filter(categoria=4).values('month').annotate(c=Sum('valor_pagamento')).values(
        'month', 'c').order_by('-month')
    mensalLocacao = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(
        data_pagamento__lte=data_atual).filter(data_pagamento__lt=data_atual).filter(categoria=5).values(
        'month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('-month')
    mensalInstalacao = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(
        data_pagamento__lte=data_atual).filter(categoria=6).values('month').annotate(c=Sum('valor_pagamento')).values(
        'month', 'c').order_by('-month')
    mensalSocios = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(
        data_pagamento__lte=data_atual).filter(categoria=7).values('month').annotate(c=Sum('valor_pagamento')).values(
        'month', 'c').order_by('-month')
    mensalImpostos = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(
        data_pagamento__lte=data_atual).filter(categoria=8).values('month').annotate(c=Sum('valor_pagamento')).values(
        'month', 'c').order_by('-month')
    mensalTaxas = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(
        data_pagamento__lte=data_atual).filter(categoria=11).values('month').annotate(c=Sum('valor_pagamento')).values(
        'month', 'c').order_by('-month')

    # Query para o mês atual das categorias de custos
    atualMensalVeiculos = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(
        data_pagamento__month=this_month).filter(status_pago=True).filter(categoria=1).values('month').annotate(
        c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    atualMensalFuncionarios = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(
        data_pagamento__month=this_month).filter(status_pago=True).filter(categoria=2).values('month').annotate(
        c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    atualMensalAlimentacao = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(
        data_pagamento__month=this_month).filter(status_pago=True).filter(categoria=3).values('month').annotate(
        c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    atualMensalLinks = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(
        data_pagamento__month=this_month).filter(status_pago=True).filter(categoria=4).values('month').annotate(
        c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    atualMensalLocacao = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(
        data_pagamento__month=this_month).filter(status_pago=True).filter(categoria=5).values('month').annotate(
        c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    atualmensalInstalacao = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(
        data_pagamento__month=this_month).filter(status_pago=True).filter(categoria=6).values('month').annotate(
        c=Sum('valor_pagamento')).values('month', 'c').order_by('month')
    atualMensalSocios = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(
        data_pagamento__month=this_month).filter(status_pago=True).filter(categoria=7).values('month').annotate(
        c=Sum('valor_pagamento')).values('month', 'c').order_by('month')

    return render(request, 'payment/index.html', {'pagamentos': pagamentos, 'dia': dia, 'mes': mes,
                                                  'veiculos': veiculos,
                                                  'funcionarios': funcionarios,
                                                  'alimentacao': alimentacao,
                                                  'links': links,
                                                  'locacao': locacao,
                                                  'instalacao': instalacao,
                                                  'socios': socios,

                                                  'atualMensalVeiculos': atualMensalVeiculos,
                                                  'atualMensalFuncionarios': atualMensalFuncionarios,
                                                  'atualMensalAlimentacao': atualMensalAlimentacao,
                                                  'atualMensalLinks': atualMensalLinks,
                                                  'atualMensalLocacao': atualMensalLocacao,
                                                  'atualmensalInstalacao': atualmensalInstalacao,
                                                  'atualMensalSocios': atualMensalSocios,

                                                  'veiculosMesAtual': veiculosMesAtual,
                                                  'funcionariosMesAtual': funcionariosMesAtual,
                                                  'alimentacaoMesAtual': alimentacaoMesAtual,
                                                  'linksMesAtual': linksMesAtual,
                                                  'locacaoMesAtual': locacaoMesAtual,
                                                  'instalacaoMesAtual': instalacaoMesAtual,
                                                  'sociosMesAtual': sociosMesAtual,
                                                  'ImpostosMesAtual': ImpostosMesAtual,
                                                  'taxaMesAtual': taxaMesAtual,

                                                  'mensalVeiculos': mensalVeiculos,
                                                  'mensalFuncionarios': mensalFuncionarios,
                                                  'mensalAlimentacao': mensalAlimentacao,
                                                  'mensalLinks': mensalLinks,
                                                  'mensalLocacao': mensalLocacao,
                                                  'mensalInstalacao': mensalInstalacao,
                                                  'mensalSocios': mensalSocios,
                                                  'mensalImpostos': mensalImpostos,
                                                  'mensalTaxas': mensalTaxas,

                                                  'custo_mes': custo_mes,
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
    return render(request, 'payment/cadastrar-pagamento.html', {'form': form})


def DashboardPagamentos(request):
    return render(request, 'payment/dashboard-pagamentos.html')


def ListaPagamentos(request):
    data_atual = datetime.now()

    data = request.GET.get('data')
    motivoPagamento = request.GET.get('motivoPagamento')
    banco = request.GET.get('banco')
    valor = request.GET.get('valor')
    startdate = request.GET.get('startdate')
    enddate = request.GET.get('enddate')

    # Show payment per bank
    if data:
        pagamentos = Pagamento.objects.filter(data_pagamento__lte=data_atual).filter(Q(data_pagamento__icontains=data))\
            .order_by('-data_pagamento')

    # Show payment per time course
    elif startdate and enddate:
        pagamentos = Pagamento.objects.filter(data_pagamento__lte=data_atual).filter(
            Q(data_pagamento__range=[startdate, enddate])).order_by('-data_pagamento')

        # Show payment per time, course and value
    elif startdate and enddate and valor:
        pagamentos = Pagamento.objects.filter(Q(data_pagamento__range=[startdate, enddate]) |
                                              Q(valor_pagamento__icontains=valor)).\
            order_by('-data_pagamento')
    # Show payment per time, course and value
    elif startdate and enddate and banco:
        pagamentos = Pagamento.objects.filter(data_pagamento__lte=data_atual).filter(
            Q(data_pagamento__range=[startdate, enddate]) |
            Q(origem_valor_pagamento__exact=banco)).order_by('-data_pagamento')
    # Show payment per reason
    elif motivoPagamento:
        pagamentos = Pagamento.objects.filter(data_pagamento__lte=data_atual).filter(
            Q(motivo_pagamento__icontains=motivoPagamento)).order_by('-data_pagamento')

    # Show payment per bank
    elif banco:
        pagamentos = Pagamento.objects.filter(data_pagamento__lte=data_atual).filter(
            Q(origem_valor_pagamento__exact=banco)).order_by('-data_pagamento')

    # Show payment per bank
    elif valor:
        pagamentos = Pagamento.objects.filter(data_pagamento__lte=data_atual).filter(
            Q(valor_pagamento__exact=valor)).order_by('-data_pagamento').order_by('-data_pagamento')

    # Show payment per value and date
    elif valor and data:
        pagamentos = Pagamento.objects.filter(data_pagamento__lte=data_atual).filter(
            Q(valor_pagamento__icontains=valor) |
            Q(data_pagamento__icontains=data)).order_by('-data_pagamento')
    else:
        # Show all payment
        pagamentos = Pagamento.objects.filter().filter(data_pagamento__lte=data_atual).order_by('-data_pagamento')

    paginator = Paginator(pagamentos, 50)  # Show 25 payment per page.
    page_number = request.GET.get('page', '1')  #
    pagamentos = paginator.get_page(page_number)
    return render(request, 'payment/lista_pagamentos.html', {'pagamentos': pagamentos})


def AgendamentosPagamentos(request):
    data_atual = datetime.now()
    vencerHoje = Pagamento.objects.filter(status_pago='False').filter(data_pagamento=data_atual)
    atrasadas = Pagamento.objects.filter(status_pago='False').filter(data_pagamento__lt=data_atual)

    naoVencidas = Pagamento.objects.filter().order_by('-data_pagamento')

    totalPagarHoje = Pagamento.objects.filter(status_pago='False').filter(data_pagamento=data_atual) \
        .aggregate(total=Sum('valor_pagamento'))
    totalPagarAtrasadas = Pagamento.objects.filter(status_pago='False').filter(data_pagamento__lt=data_atual).\
        aggregate(total=Sum('valor_pagamento'))
    totalPagarNaoVencidas = Pagamento.objects.filter(status_pago='False').filter(data_pagamento__gt=data_atual).\
        aggregate(total=Sum('valor_pagamento'))

    pagamentosFuturos = Pagamento.objects.filter(status_pago='False').annotate(month=TruncMonth('data_pagamento')).\
        values('month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')

    pagamentosFuturosDiarios = Pagamento.objects.filter(status_pago='False').values('data_pagamento').\
        annotate(number=Sum('valor_pagamento')).order_by('data_pagamento')

    return render(request, 'payment/agendamentos-pagamentos.html', {'vencerHoje': vencerHoje,
                                                                    'atrasadas': atrasadas,
                                                                    'naoVencidas': naoVencidas,
                                                                    'totalPagarHoje': totalPagarHoje,
                                                                    'totalPagarAtrasadas': totalPagarAtrasadas,
                                                                    'totalPagarNaoVencidas': totalPagarNaoVencidas,
                                                                    'pagamentosFuturos': pagamentosFuturos,
                                                                'pagamentosFuturosDiarios': pagamentosFuturosDiarios,
                                                                    })


def PagamentosFuturos(request):
    data_atual = datetime.now()
    naoVencidas = Pagamento.objects.filter(status_pago='False').filter(
        data_pagamento__gte=data_atual).order_by('data_pagamento')

    date = request.GET.get('date')
    motivoPagamento = request.GET.get('motivoPagamento')
    valor = request.GET.get('valor')

    if date and motivoPagamento:
        naoVencidas = Pagamento.objects.filter(status_pago='False'). \
            filter(data_pagamento__gt=data_atual).filter(Q(motivo_pagamento__icontains=motivoPagamento) |
                                                         Q(data_pagamento__exact=date))

    elif date:
        naoVencidas = Pagamento.objects.filter(status_pago='False'). \
            filter().filter(Q(data_pagamento__exact=date))

    elif valor:
        naoVencidas = Pagamento.objects.filter(status_pago='False'). \
            filter().filter(Q(valor_pagamento__exact=valor))

    elif motivoPagamento:
        naoVencidas = Pagamento.objects.filter(status_pago='False'). \
            filter().filter(Q(motivo_pagamento__icontains=motivoPagamento))

    return render(request, 'payment/pagamentos-futuros.html', {'naoVencidas': naoVencidas})


def PagamentosMensaisGrupos(request):
    data_atual = datetime.now()

    mensalVeiculos = Pagamento.objects.annotate(month=TruncMonth('data_pagamento')).filter(categoria=1).values(
        'month').annotate(c=Sum('valor_pagamento')).values('month', 'c').order_by('month')

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

    context = {
        'mensalVeiculos': mensalVeiculos,
    }

    return render(request, 'payment/pagamentos-mensais-grupos.html', context)


def AgendarPagamento(request):
    form = AgendarPagamentoForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Pagamento agendado com sucesso!')
        return redirect('/pagamentos/contas-a-pagar/')
    else:
        form = AgendarPagamentoForm()
    return render(request, 'payment/agendar-pagamento.html', {'form': form})


def EditarPagamento(request, id=None):
    pagar = get_object_or_404(Pagamento, id=id)
    form = EditarPagamentoForm(request.POST or None, instance=pagar)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Pagamento alterado com sucesso.')
        return redirect('/pagamentos/lista-pagamentos/')
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


def FluxoEntradaSaida(request):
    fluxos = FluxoEntradasSaidas.objects.all()
    return render(request, 'payment/fluxo-entradas-saidas.html', {'fluxos': fluxos})


class FluxoCreate(CreateView):
    model = FluxoEntradasSaidas
    form_class = CadastrarFluxoForm
    template_name = 'payment/cadastrar-fluxo-entradas-saidas.html'
    success_url = '/pagamentos/fluxo-entradas-saidas/'


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


def SalvarPagamento(request):
    form = CadastarPagamentoForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Pagamento adicionado com sucesso!')
        return redirect('/pagamentos/')
    else:
        form = CadastarPagamentoForm()
    return render(request, 'payment/salvar-pagamento.html', {'form': form})


# ---------------------------------- Movimentações do ReceitaNET -------------------------------------------------------
def RetiradasGerencianet(request):
    startdate = request.GET.get('startdate')
    enddate = request.GET.get('enddate')

    if startdate and enddate:
        retiradas = DestinoValoresBoletos.objects.filter(
            data_transacao__range=[startdate, enddate]).order_by('-data_transacao')
    else:
        retiradas = DestinoValoresBoletos.objects.all().order_by('-data_transacao')

    valor_mes = DestinoValoresBoletos.objects.annotate(month=TruncMonth('data_transacao')).values('month').annotate(
        c=Sum('valor')).values('month', 'c').order_by('-month')

    context = {
        'retiradas': retiradas,
        'valor_mes': valor_mes,
    }
    return render(request, 'payment/lista-retiradas-gerencianet.html', context)


class RetiradasGerencianetCreateView(SuccessMessageMixin, CreateView):
    model = DestinoValoresBoletos
    template_name = "payment/cadastrar-valores-receitanet.html"
    form_class = CadastarDestinoValoresBoletosForm
    success_url = '/pagamentos/retiradas-gerencianet/'
    success_message = "R$: %(valor)s, foi cadastrado com sucesso!!!"


class RetiradasGerencianetUpdateView(UpdateView):
    model = DestinoValoresBoletos  # A tabela do banco de dados
    form_class = EditarDestinoValoresBoletosForm  # Form for Update
    template_name = 'payment/editar-valores-receitanet.html'  # templete for updating
    template_name_suffix = 'editar-valores-receitanet'
    success_url = "/pagamentos/retiradas-gerencianet/"  # return após atualizar


# Exportando os dados para CSV
def ExportarRetiradasReceitanetCSV():
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="relatorio-retiradas-receitanet.csv"'
    retiradas = DestinoValoresBoletos.objects.all()
    writer = csv.writer(response)
    writer.writerow(['id', 'valor', 'destino', 'data_transacao'])
    for pag in retiradas:
        writer.writerow([pag.id, pag.data_pagamento, pag.motivo_pagamento, pag.valor_pagamento,
                         pag.origem_valor_pagamento, pag.tipo_custo_pagamento, pag.categoria, pag.status_pago
                         ])
    return response


# ----------------------------- BOLETOS-------------------------------------------------
class EntregaBoletosListView(ListView):
    model = ClientesEntregaBoletos
    template_name = 'payment/lista-entrega-boletos.html'  # templete for updating

    def get_context_data(self, **kwargs):
        context = super(EntregaBoletosListView, self).get_context_data(**kwargs)

        context['count_via_fisica'] = ClientesEntregaBoletos.objects.filter(forma_entrega=1).count()
        context['count_email_whatsapp'] = ClientesEntregaBoletos.objects.filter(forma_entrega=2).count()
        context['count_app'] = ClientesEntregaBoletos.objects.filter(forma_entrega=3).count()
        context['count_whatsapp'] = ClientesEntregaBoletos.objects.filter(forma_entrega=4).count()
        context['count_email'] = ClientesEntregaBoletos.objects.filter(forma_entrega=5).count()

        queryset = self.request.GET.get('q')
        forma_entrega_boleto = self.request.GET.get('forma_entrega_boleto')

        if queryset:
            context['lista_boletos_entregue'] = ClientesEntregaBoletos.objects.filter(
                Q(nome_cliente__icontains=queryset)).order_by('nome_cliente')
            context['count_boletos_entregue'] = ClientesEntregaBoletos.objects.filter(
                Q(nome_cliente__icontains=queryset)).count()
        elif forma_entrega_boleto:
            context['lista_boletos_entregue'] = ClientesEntregaBoletos.objects.filter(
                Q(forma_entrega__exact=forma_entrega_boleto)).order_by('nome_cliente')
            context['count_boletos_entregue'] = ClientesEntregaBoletos.objects.filter(
                Q(forma_entrega__exact=forma_entrega_boleto)).count()
        else:
            context['lista_boletos_entregue'] = ClientesEntregaBoletos.objects.all().order_by('nome_cliente')
            context['count_boletos_entregue'] = ClientesEntregaBoletos.objects.all().count()
        return context


class EntregaBoletosCreateView(SuccessMessageMixin, CreateView):
    model = ClientesEntregaBoletos
    template_name = "payment/cadastrar-entrega-boletos.html"
    form_class = ClientesEntregaBoletosForm
    success_url = '/pagamentos/lista-entrega-boletos/'
    success_message = "%(nome_cliente)s, foi cadastrado com sucesso!!!"


class EditarEntregaBoletosUpdateView(UpdateView):
    model = ClientesEntregaBoletos  # A tabela do banco de dados
    form_class = EditarClientesEntregaBoletosForm  # Form for Update
    template_name = 'payment/editar-entrega-boletos.html'  # templete for updating
    success_url = "/pagamentos/lista-entrega-boletos/"  # return após atualizar
    success_message = "foi atualizado com sucesso!!!"
