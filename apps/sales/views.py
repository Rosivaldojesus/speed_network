from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q, Sum, Count
from django.db.models.functions import TruncMonth, ExtractMonth
from datetime import datetime, date, timedelta
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from ..sales.funcoes.dados_instalacoes import *
from .models import Instalacao, ValeRefeicao, Cancelamentos
from ..components.models import FuncionariosParaVale, Vendedores
from ..services.models import ServicoVoip
from .forms import *
import csv

# Create your views here.

@login_required(login_url='/login/')
def Index(request):
    template_name = 'sales/instalacao.html'
    quant_aberta = quantidade_instalacoes_em_aberto()
    quant_agendada = quantidade_instalacoes_agendadas()
    quant_sem_boleto = quantidade_instalacoes_sem_boleto()
    quant_concluida = quantidade_instalacoes_mes_atual()

    #  Instalações Mensais
    instalacoes_mensais = quantidade_instalacoes_mensais()
    instalacoes_diarias = quantidade_instalacoes_diarias()

    # Como o cliente conheceu a empresa
    conheceu_empresa_count = quantidade_conheceu_empresa_count()
    conheceu_empresa_mes_count = quantidade_conheceu_empresa_mes_count()
    panfletos_count = quantidade_conheceu_por_panfletos()

    #  Filtros de como o cliente conheceu a empresa
    redes_sociais_count = conheceu_redes_sociais_count()
    site_count = conheceu_site_count()
    indicacao_count = conheceu_indicacao_count()
    outros_count = conheceu_outros_count()

    #  Filtros de como o cliente conheceu a empresa mês atual
    panfletos_mes_count = conheceu_panfletos_mes_count()
    redes_sociais_mes_count = conheceu_redes_sociais_mes_count()
    site_mes_count = conheceu_site_mes_count()
    indicacao_mes_count = conheceu_indicacao_mes_count()
    outros_mes_count = conheceu_empresa_outros_mes_count()

    context = {
        'quant_aberta': quant_aberta,
        'quant_agendada': quant_agendada,
        'quant_concluida': quant_concluida,
        'quant_sem_boleto': quant_sem_boleto,
        'instalacoes_mensais': instalacoes_mensais,
        'instalacoes_diarias': instalacoes_diarias,

        #  Filtros de como o cliente conheceu a empresa
        'conheceu_empresa_count': conheceu_empresa_count,
        'panfletos_count': panfletos_count,
        'redes_sociais_count': redes_sociais_count,
        'site_count': site_count,
        'indicacao_count': indicacao_count,
        'outros_count': outros_count,
        'panfletos_mes_count': panfletos_mes_count,
        'redes_sociais_mes_count': redes_sociais_mes_count,
        'site_mes_count': site_mes_count,
        'indicacao_mes_count': indicacao_mes_count,
        'outros_mes_count': outros_mes_count,
        'conheceu_empresa_mes_count': conheceu_empresa_mes_count,
    }
    return render(request, template_name, context)


@login_required(login_url='/login/')
def VendasInstalacao(request):
    vendedores = Vendedores.objects.all()
    vendas = Instalacao.objects.all().order_by('-id')
    queryset = request.GET.get('q')
    if queryset:
        vendas = Instalacao.objects.filter(Q(instalacao_vendedor__icontains=queryset))
    conetxt = {
        'vendas': vendas,
        'vendedores': vendedores
    }
    return render(request, 'sales/vendas-instalacao.htyml', conetxt)


@login_required(login_url='/login/')
def InstalacaoAberta(request):
    user = request.user
    abertas = Instalacao.objects.filter(status_agendada='False').filter(concluido='False')
    quant_aberta = Instalacao.objects.filter(status_agendada='False').filter(concluido='False').count()
    #  Filtro por vendedor logado
    abertas_vendedor = Instalacao.objects.filter(instalacao_criado_por=user).filter(status_agendada='False')\
        .filter(concluido='False')
    quant_aberta_vendedor = Instalacao.objects.filter(instalacao_criado_por=user).filter(status_agendada='False')\
        .filter(concluido='False').count()
    context = {
        'abertas': abertas,
        'quant_aberta': quant_aberta,
        'abertas_vendedor': abertas_vendedor,
        'quant_aberta_vendedor': quant_aberta_vendedor,
    }
    return render(request, 'sales/instalacao-aberta.html', context)


@login_required(login_url='/login/')
def InstalacaoAgendada(request):
    agendadas = Instalacao.objects.filter(status_agendada='True')\
        .filter(concluido='False').order_by('data_instalacao', 'hora_instalacao')
    quant_agendada = Instalacao.objects.filter(status_agendada='True').filter(concluido='False').count()
    queryset = request.GET.get('q')
    data_dia = request.GET.get('data_dia')
    if queryset:
        agendadas = Instalacao.objects.\
            filter(Q(nome_cliente__icontains=queryset) | Q(sobrenome_cliente__icontains=queryset)).\
            filter(status_agendada='True').filter(concluido='False').order_by('data_instalacao', 'hora_instalacao')
    elif data_dia:
        agendadas = Instalacao.objects.filter(Q(data_instalacao__exact=data_dia))
        quant_agendada = Instalacao.objects.filter(Q(data_instalacao__exact=data_dia)).count()
    context = {
        'agendadas': agendadas,
        'quant_agendada': quant_agendada,
    }
    return render(request, 'sales/instalacao-agendada.html', context)


@login_required(login_url='/login/')
def InstalacaoConcluida(request):
    quant_concluida = Instalacao.objects.filter(concluido='True').count()
    concluidas = Instalacao.objects.filter(concluido='True').order_by('-id')
    startdate = request.GET.get('startdate')
    queryset = request.GET.get('q')
    date = request.GET.get('date')
    if queryset:
        concluidas = Instalacao.objects.\
            filter(Q(nome_cliente__icontains=queryset) | Q(sobrenome_cliente__icontains=queryset))
        quant_concluida = Instalacao.objects.\
            filter(Q(nome_cliente__icontains=queryset) | Q(sobrenome_cliente__icontains=queryset)).count()
    elif date:
        concluidas = Instalacao.objects.filter(Q(data_finalizacao__exact=date))
        quant_concluida = Instalacao.objects.filter(Q(data_finalizacao__exact=date)).count()
    elif startdate:
        concluidas = Instalacao.objects.filter(Q(data_agendada__exact=startdate))
    context = {
        'concluidas': concluidas,
        'quant_concluida': quant_concluida
    }
    return render(request, 'sales/instalacao-concluida.html', context)


@login_required(login_url='/login/')
def InstalacaoConcluidaVendedores(request):
    concluidas = Instalacao.objects.filter(concluido='True').order_by('-id')
    quant_concluida = Instalacao.objects.filter(concluido='True').count()
    startdate = request.GET.get('startdate')
    enddate = request.GET.get('enddate')
    queryset = request.GET.get('q')
    if startdate and enddate and queryset:
        concluidas = Instalacao.objects.filter(concluido='True').\
            filter(Q(data_instalacao__range=[startdate, enddate]) & Q(instalacao_vendedor__exact=queryset)).\
            order_by('data_instalacao')
        quant_concluida = Instalacao.objects.filter(concluido='True').\
            filter(Q(data_instalacao__range=[startdate, enddate]) & Q(instalacao_vendedor__exact=queryset)).count()
    context = {
        'concluidas': concluidas,
        'quant_concluida': quant_concluida
    }
    return render(request, 'sales/instalacao-concluida-vendedores.html', context)


@login_required(login_url='/login/')
def CadastroInstalacao(request):
    form = InstalacaoCreateForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.instalacao_criado_por = request.user
        obj.save()
        messages.success(request, 'Instalação cadastrada com sucesso.')
        return redirect('/vendas/')
    else:
        form = InstalacaoCreateForm()
    return render(request, 'sales/cadastro-instalacao.html', {'form': form})


@login_required(login_url='/login/')
def InstalacaoVisualizacao(request):
    install = request.GET.get('id')
    if install:
        install = Instalacao.objects.get(id=install)
    return render(request, 'sales/visualizar-instalacao.html', {'install': install})


@login_required(login_url='/login/')
def InstalacaoEditar(request, id=None):
    try:
        insta = get_object_or_404(Instalacao, id=id)
        form = InstalacaoUpdateForm(request.POST or None, instance=insta)
        if form.is_valid():
            obj = form.save()
            obj.save()
            messages.success(request, 'Instalação editada com sucesso.')
            return redirect('/vendas/')
    except:
        return HttpResponseNotFound("error 404") 
    return render(request, 'sales/editar-instalacao.html', {'form': form})


@login_required(login_url='/login/')
def InstalacaoAgendar(request, id=None):
    try:
        insta = get_object_or_404(Instalacao, id=id)
        form = InstalacaoAgendarForm(request.POST or None, instance=insta)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.status_agendada = True
            obj = form.save()
            obj.save()
            messages.success(request, 'Instalação agendada com sucesso.')
            return redirect('/vendas/')
    except:
        return HttpResponseNotFound("error 404")

    return render(request, 'sales/agendar-instalacao.html', {'form': form})


@login_required(login_url='/login/')
def DeletarInstalacaoAgendada(request, id=None):
    try:
        install = get_object_or_404(Instalacao, id=id)
        if request.method == "POST":
            install.delete()
            return redirect('/vendas/')
    except:
        return HttpResponseNotFound("error 404")
    return render(request, 'sales/deletar-instalacao-agendada.html', {'install': install})



@login_required(login_url='/login/')
def InstalacaoSemBoleto(request):
    try:
        boletos = Instalacao.objects.filter(status_agendada='True')
        context = {'boletos': boletos }
    except:
        return HttpResponseNotFound("error 404")
    return render(request, 'sales/instalacao-sem-boleto.html', context)



@login_required(login_url='/login/')
def InstalacaoFinalizadaSemBoleto(request):
    try:
        concluidas = Instalacao.objects.filter(concluido='True').filter(boleto_entregue='False')
        quant_sem_boleto = Instalacao.objects.filter(concluido='True').filter(boleto_entregue='False').count()
        context = {
            'concluidas': concluidas,
            'quant_sem_boleto': quant_sem_boleto,
        }
    except:
        return HttpResponseNotFound("error 404")
    return render(request, 'sales/instalacao-finalizada-sem-boleto.html', context)


@login_required(login_url='/login/')
def InstalacaoFinalizar(request, id=None):
    try:
        insta = get_object_or_404(Instalacao, id=id)
        form = InstalacaoFinalizarForm(request.POST or None, instance=insta)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.instalacao_finalizado_por = request.user
            obj = form.save()
            obj.save()
            messages.success(request, 'Instalação finalizada com sucesso.')
            return redirect('/vendas/')
    except:
        return HttpResponseNotFound("error 404")
    return render(request, 'sales/finalizar-instalacao.html', {'form': form})


@login_required(login_url='/login/')
def FinalizarEntregaBoleto(request, id=None):
    boleto = get_object_or_404(Instalacao, id=id)
    form = BoletoEntregueForm(request.POST or None, instance=boleto)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Boleto finalizado com sucesso.')
        return redirect('/vendas/')
    return render(request, 'sales/finalizar-boleto.html', {'form': form})


# Exportando relatório de vendas por vendedor
def ExportarReletarioVendasVendedor(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="relatorio-vendas.csv"'

    vendas = Instalacao.objects.filter()
    writer = csv.writer(response)
    writer.writerow(['nome_cliente', 'cpf_cliente','data_instalacao','planos_instalacao' , 'instalacao_vendedor'
    ])
    for venda in vendas:
       writer.writerow([venda.nome_cliente, venda.cpf_cliente,venda.data_instalacao, venda.planos_instalacao,  venda.instalacao_vendedor])
    return response
#  ------------------------------------  SERVIÇOS VOIP  -------------------------------------


@login_required(login_url='/login/')
def Voip(request):
    VendaMes = ServicoVoip.objects.annotate(month=TruncMonth('data_reserva_voip')).filter().values('month').\
        annotate(c=Count('data_reserva_voip')).values('month', 'c').order_by('month')
    quant_numeros_novos = ServicoVoip.objects.filter(portabilidade_voip='False').count()
    quant_numeros_portabilidade = ServicoVoip.objects.filter(portabilidade_voip='True').count()
    context = {
        'quant_numeros_novos': quant_numeros_novos,
        'quant_numeros_portabilidade': quant_numeros_portabilidade,
        'VendaMes': VendaMes,
    }
    return render(request, 'sales/voip.html', context)


@login_required(login_url='/login/')
def ClientesVoip(request):
    clientes = ServicoVoip.objects.filter(reservado_voip='True')
    quant_clientes_ativo = ServicoVoip.objects.filter(reservado_voip='True').count()
    context = {
        'clientes': clientes,
        'quant_clientes_ativo': quant_clientes_ativo,
    }
    return render(request, 'sales/clientes-voip.html', context)


def VoipFinalizadoSemBoleto(request):
    quant_sem_boleto = ServicoVoip.objects.filter(boleto_entregue='False').count()
    concluidos = ServicoVoip.objects.all()
    context = {
        'quant_sem_boleto': quant_sem_boleto,
        'concluidos': concluidos
    }
    return render(request, 'sales/voip-finalizado-sem-boleto.html', context)


#  ------------------------------------  VALES  -------------------------------------
def ValeRefeicoes(request):
    vales_sem_valor = ValeRefeicao.objects.filter(valor_vale__isnull=True)
    vales_com_valor = ValeRefeicao.objects.filter(valor_vale__isnull=False).filter(status_pago=False)
    valor_pagar = ValeRefeicao.objects.filter(status_pago=False).filter().aggregate(Sum('valor_vale')).\
        get('valor_vale__sum')
    startdate = request.GET.get('startdate')
    enddate = request.GET.get('enddate')
    queryset = request.GET.get('q')
    if startdate and enddate and queryset:
        vales_com_valor = ValeRefeicao.objects.filter(status_pago=False).\
            filter(Q(data_vale__range=[startdate, enddate]) & Q(nome_funcionario__icontains=queryset))
        valor_pagar = ValeRefeicao.objects.filter(status_pago=False).filter(Q(nome_funcionario__icontains=queryset)).\
            aggregate(Sum('valor_vale')).get('valor_vale__sum')
    elif queryset:
        vales_com_valor = ValeRefeicao.objects.filter(status_pago=False).filter(Q(nome_funcionario__icontains=queryset))
        valor_pagar = ValeRefeicao.objects.filter(status_pago=False).filter(Q(nome_funcionario__icontains=queryset)).\
            aggregate(Sum('valor_vale')).get('valor_vale__sum')
    context = {
        'vales_sem_valor': vales_sem_valor,
        'vales_com_valor': vales_com_valor,
        'valor_pagar': valor_pagar,
    }
    return render(request, 'sales/vale-refeicao.html', context)


class EmitirValeRefeicaoCreate(SuccessMessageMixin, CreateView):
    model = ValeRefeicao
    form_class = EmitirValeRefeicaoForm
    success_url = '/vendas/vale-refeicao/'
    success_message = 'Vale emitido com sucesso!!!!'


class AdicionarNomeParaValeCreate(CreateView):
    model = FuncionariosParaVale
    fields = ['nome_funcionario']
    success_url = '/vendas/vale-refeicao/'
    success_message = 'Nome adicionado com sucesso!!!!'


def AdicionarValorVale(request, id=None):
    vale = get_object_or_404(ValeRefeicao, id=id)
    form = AdicionarValorValeRefeicaoForm(request.POST or None, instance=vale)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Valor adicionado com sucesso.')
        return redirect('/vendas/vale-refeicao/')
    return render(request, 'sales/adicionar-valor-vale.html', {'form': form})


def AdicionarPagamentoVale(request, id=None):
    vale = get_object_or_404(ValeRefeicao, id=id)
    form = AdicionarPagamentoValeRefeicaoForm(request.POST or None, instance=vale)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Pagamento concluído.')
        return redirect('/vendas/vale-refeicao/')
    return render(request, 'sales/adicionar-pagamento-vale.html', {'form': form})

#  --------------------- Cancellations -------------------------------------------------
class CancelamentosCreateView(CreateView, SuccessMessageMixin):
    model = Cancelamentos
    form_class = CadastrarCancelamentosForm
    template_name = 'sales/cadastrar-cancelamentos.html'
    success_url = '/vendas/'
    success_message = "%(nome), foi cancelado corretamente."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, nome=self.object.nome)

    def form_valid(self, form):
        form.instance.atendente = self.request.user
        return super().form_valid(form)


class CancelamentosListView(ListView):
    model = Cancelamentos
    template_name = 'sales/lista-cancelamentos.html'

    def get_context_data(self, **kwargs):
        context = super(CancelamentosListView, self).get_context_data(**kwargs)
        this_month = date.today().month

        context['cancelamentos'] = Cancelamentos.objects.all()
        context['count_cancelamentos'] = Cancelamentos.objects.all().count()
        context['cancelamentos_mensais'] = Cancelamentos.objects.annotate(month=TruncMonth('data')).values('month').\
            annotate(total=Count('month')).values('month', 'total').order_by('month')

        # Cancelamentos por plano no mês atual
        context['plano_100mb_mes_atual'] = Cancelamentos.objects.filter(data__month=this_month).\
            filter(plano_internet__icontains='69,90').count()
        context['plano_200mb_mes_atual'] = Cancelamentos.objects.filter(data__month=this_month).\
            filter(plano_internet__icontains='89,90').count()
        context['plano_400mb_mes_atual'] = Cancelamentos.objects.filter(data__month=this_month).\
            filter(plano_internet__icontains='99,90').count()
        context['plano_500mb_mes_atual'] = Cancelamentos.objects.filter(data__month=this_month).\
            filter(plano_internet__icontains='119,90').count()
        context['plano_600mb_mes_atual'] = Cancelamentos.objects.filter(data__month=this_month).\
            filter(plano_internet__icontains='149,90').count()

        # Cancelamentos por plano
        context['plano_100mb'] = Cancelamentos.objects.filter(plano_internet__icontains='69,90').count()
        context['plano_200mb'] = Cancelamentos.objects.filter(plano_internet__icontains='89,90').count()
        context['plano_400mb'] = Cancelamentos.objects.filter(plano_internet__icontains='99,90').count()
        context['plano_500mb'] = Cancelamentos.objects.filter(plano_internet__icontains='119,90').count()
        context['plano_600mb'] = Cancelamentos.objects.filter(plano_internet__icontains='149,90').count()

        # Cancelamentos por plano
        context['plano_69'] = Cancelamentos.objects.filter(plano_internet__icontains='69,90').count()
        context['plano_89'] = Cancelamentos.objects.filter(plano_internet__icontains='89,90').count()
        context['plano_99'] = Cancelamentos.objects.filter(plano_internet__icontains='99,90').count()
        context['plano_119'] = Cancelamentos.objects.filter(plano_internet__icontains='119,90').count()
        context['plano_149'] = Cancelamentos.objects.filter(plano_internet__icontains='149,90').count()

        return context


class CancelamentosUpdateView(UpdateView):
    model = Cancelamentos
    form_class = EditarCancelamentosForm
    template_name = 'sales/editar-cancelamento.html'
    template_name_suffix = 'editar-cancelamento'
    success_url = '/vendas/lista-cancelamentos/'
