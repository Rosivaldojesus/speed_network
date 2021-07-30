from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum, Count
from .models import Instalacao, ValeRefeicao
from ..components.models import FuncionariosParaVale
from ..services.models import ServicoVoip
from .forms import InstalacaoCreateForm, InstalacaoUpdateForm,\
    InstalacaoAgendarForm, InstalacaoFinalizarForm, BoletoEntregueForm,\
    InstalacaoDefinirTecnicoForm, EmitirValeRefeicaoForm, AdicionarValorValeRefeicaoForm
from ..components.models import Vendedores
from django.db.models.functions import ExtractMonth
from django.db.models.functions import TruncMonth
from django.views.generic.edit import CreateView


# Create your views here.
@login_required(login_url='/login/')
def Index(request):
    instalacoes = Instalacao.objects.all().order_by('data_instalacao', 'data_instalacao')
    quant_aberta = Instalacao.objects.filter(status_agendada='False').filter(concluido='False').count()
    quant_agendada = Instalacao.objects.filter(status_agendada='True').filter(concluido='False').count()
    quant_sem_boleto = Instalacao.objects.filter(concluido='True').filter(boleto_entregue='False').count()
    quant_concluida = Instalacao.objects.filter(concluido='True').count()
    #Filtrando instalação por Vendedor
    user = request.user
    instalacaoVendedor = Instalacao.objects.filter(instalacao_criado_por=user)
    quant_aberta_vendedor = Instalacao.objects.filter(instalacao_criado_por=user).filter(status_agendada='False')\
        .filter(concluido='False').count()
    quant_agendada_vendedor = Instalacao.objects.filter(instalacao_criado_por=user).filter(status_agendada='True')\
        .filter(concluido='False').count()
    #Instalações Mensais
    instalacoesMensais = Instalacao.objects.annotate(month=ExtractMonth('data_finalizacao')).values('month').annotate(count=Count('id'))
    mensalInstalacao = Instalacao.objects.annotate(month=TruncMonth('data_finalizacao')).filter(concluido='True').values('month').annotate(c=Count('data_finalizacao')).values('month', 'c').order_by('month')
    diarioInstalaçao = Instalacao.objects.filter(concluido='True').values('data_finalizacao').annotate( number=Count('data_finalizacao')).order_by('data_finalizacao')[40:]

    return render(request, 'sales/instalacao.html', {'instalacoes': instalacoes,
                                                     'quant_aberta': quant_aberta,
                                                     'quant_agendada': quant_agendada,
                                                     'quant_concluida': quant_concluida,
                                                     'quant_sem_boleto': quant_sem_boleto,
                                                     # Filtrando instalação por Vendedor
                                                     'instalacaoVendedor': instalacaoVendedor,
                                                     'quant_aberta_vendedor':quant_aberta_vendedor,
                                                     'quant_agendada_vendedor': quant_agendada_vendedor,

                                                     'instalacoesMensais': instalacoesMensais,

                                                     'mensalInstalacao':mensalInstalacao,
                                                     'diarioInstalaçao':diarioInstalaçao,
                                                     })

@login_required(login_url='/login/')
def VendasInstalacao(request):
    vendedores = Vendedores.objects.all()
    vendas = Instalacao.objects.all().order_by('-id')
    queryset = request.GET.get('q')
    if queryset:
        vendas = Instalacao.objects.filter(
            Q(instalacao_vendedor__icontains=queryset))

    return render(request, 'sales/vendas-instalacao.htyml', {'vendas': vendas,
                                                            'vendedores': vendedores})

@login_required(login_url='/login/')
def InstalacaoAberta(request):
    user = request.user
    abertas = Instalacao.objects.filter(status_agendada='False').filter(concluido='False')
    quant_aberta = Instalacao.objects.filter(status_agendada='False').filter(concluido='False').count()
    #Filtro por vendedor logado
    abertas_vendedor = Instalacao.objects.filter(instalacao_criado_por=user).filter(status_agendada='False')\
        .filter(concluido='False')
    quant_aberta_vendedor = Instalacao.objects.filter(instalacao_criado_por=user).filter(status_agendada='False')\
        .filter(concluido='False').count()
    return render(request, 'sales/instalacao-aberta.html', {'abertas': abertas,
                                                            'quant_aberta': quant_aberta,
                                                            #Filtro por vendedor
                                                            'abertas_vendedor':abertas_vendedor,
                                                            'quant_aberta_vendedor': quant_aberta_vendedor,
                                                        })

@login_required(login_url='/login/')
def InstalacaoAgendada(request):
    agendadas = Instalacao.objects.filter(status_agendada='True')\
        .filter(concluido='False').order_by('data_instalacao', 'hora_instalacao')
    queryset = request.GET.get('q')
    if queryset:
        agendadas = Instalacao.objects.filter(
            Q(nome_cliente__icontains=queryset)|
            Q(sobrenome_cliente__icontains=queryset)|
            Q(data_instalacao__icontains=queryset)
        ).filter(status_agendada='True')\
        .filter(concluido='False').order_by('data_instalacao', 'hora_instalacao')

    quant_agendada = Instalacao.objects.filter(status_agendada='True').filter(concluido='False').count()
    #Filtro por vendedor
    user = request.user
    agendadas_vendedor = Instalacao.objects.filter(instalacao_criado_por=user).filter(status_agendada='True') \
        .filter(concluido='False').order_by('data_instalacao', 'hora_instalacao')
    quant_agendada_vendedor = Instalacao.objects.filter(instalacao_criado_por=user).\
        filter(status_agendada='True').filter(concluido='False').count()
    return render(request, 'sales/instalacao-agendada.html', {'agendadas':agendadas,
                                                              'quant_agendada':quant_agendada,
                                                              #Filtro por vendedor
                                                              'agendadas_vendedor':agendadas_vendedor,
                                                              'quant_agendada_vendedor':quant_agendada_vendedor,
                                                              })

@login_required(login_url='/login/')
def InstalacaoConcluida(request):
    concluidas = Instalacao.objects.filter(concluido='True').order_by('-id')
    queryset = request.GET.get('q')
    if queryset:
        concluidas = Instalacao.objects.filter(
            Q(nome_cliente__icontains=queryset) |
            Q(sobrenome_cliente__icontains=queryset))

    quant_concluida = Instalacao.objects.filter(concluido='True').count()
    return render(request, 'sales/instalacao-concluida.html', {'concluidas': concluidas,
                                                               'quant_concluida':quant_concluida
                                                               })
'''
@login_required(login_url='/login/')
def InstalacaoConcluidaVendedores(request):
    concluidas = Instalacao.objects.filter(concluido='True').order_by('-id')
    queryset = request.GET.get('q')
    queryset1 = request.GET.get('q1')
    if queryset:
        concluidas = Instalacao.objects.filter(Q(instalacao_vendedor__exact=queryset) & Q(nome_cliente__icontains=queryset1))

    quant_concluida = Instalacao.objects.filter(concluido='True').count()
    return render(request, 'sales/instalacao-concluida-vendedores.html', {'concluidas': concluidas,
                                                               'quant_concluida':quant_concluida
                                                               })

'''
@login_required(login_url='/login/')
def InstalacaoConcluidaVendedores(request):
    concluidas = Instalacao.objects.filter(concluido='True').order_by('-id')
    quant_concluida = Instalacao.objects.filter(concluido='True').count()
    startdate = request.GET.get('startdate')
    enddate = request.GET.get('enddate')
    queryset = request.GET.get('q')
    if startdate and enddate and queryset:
        concluidas = Instalacao.objects.filter(Q(data_instalacao__range=[startdate, enddate])
                                               & Q(instalacao_vendedor__exact=queryset))
        quant_concluida = Instalacao.objects.filter(Q(data_instalacao__range=[startdate, enddate])
                                               & Q(instalacao_vendedor__exact=queryset)).count()

    return render(request, 'sales/instalacao-concluida-vendedores.html', {'concluidas': concluidas,
                                                               'quant_concluida':quant_concluida
                                                               })

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
    return render(request, 'sales/visualizar-instalacao.html',{'install': install})


@login_required(login_url='/login/')
def InstalacaoEditar(request, id=None):
    insta = get_object_or_404(Instalacao, id=id)
    form = InstalacaoUpdateForm(request.POST or None, instance=insta)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Instalação editada com sucesso.')
        return redirect('/vendas/')
    return render(request, 'sales/editar-instalacao.html', {'form': form})


@login_required(login_url='/login/')
def InstalacaoAgendar(request, id=None):
    insta = get_object_or_404(Instalacao, id=id)
    form = InstalacaoAgendarForm(request.POST or None, instance=insta)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Instalação agendada com sucesso.')
        return redirect('/vendas/instalacao-agendada/')
    return render(request, 'sales/agendar-instalacao.html', {'form': form})


def DeletarInstalacaoAgendada(request, id=None):
    install = get_object_or_404(Instalacao, id=id)
    if request.method == "POST":
        install.delete()
        return redirect('/vendas/')
    return render(request, 'sales/deletar-instalacao-agendada.html', {'install': install})


@login_required(login_url='/login/')
def InstalacaoDefinirTecnico(request, id=None):
    defenir = get_object_or_404(Instalacao, id=id)
    form = InstalacaoDefinirTecnicoForm(request.POST or None, instance=defenir)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Técnico defenido com sucesso.')
        return redirect('/vendas/')
    return render(request, 'sales/agendar-instalacao.html', {'form': form})


@login_required(login_url='/login/')
def InstalacaoSemBoleto(request):
    boletos = Instalacao.objects.filter(status_agendada='True')
    return render(request, 'sales/instalacao-sem-boleto.html')


@login_required(login_url='/login/')
def InstalacaoFinalizadaSemBoleto(request):
    concluidas = Instalacao.objects.filter(concluido='True').filter(boleto_entregue='False')
    quant_sem_boleto = Instalacao.objects.filter(concluido='True').filter(boleto_entregue='False').count()
    return render(request, 'sales/instalacao-finalizada-sem-boleto.html', {'concluidas':concluidas,
                                                                           'quant_sem_boleto': quant_sem_boleto,
                                                                           })

@login_required(login_url='/login/')
def InstalacaoFinalizar(request, id=None):
    insta = get_object_or_404(Instalacao, id=id)
    form = InstalacaoFinalizarForm(request.POST or None, instance=insta)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.instalacao_finalizado_por = request.user
        obj = form.save()
        obj.save()
        messages.success(request, 'Instalação finalizada com sucesso.')
        return redirect('/vendas/')
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

#------------------------------------  SERVIÇOS VOIP  -------------------------------------

def Voip(request):
    VendaMes =  ServicoVoip.objects.annotate(month=TruncMonth('data_reserva_voip')).filter().values('month').annotate(c=Count('data_reserva_voip')).values('month', 'c').order_by('month')
    quant_numeros_novos = ServicoVoip.objects.filter(portabilidade_voip='False').count()
    quant_numeros_portabilidade = ServicoVoip.objects.filter(portabilidade_voip='True').count()
    return render(request, 'sales/voip.html', {'quant_numeros_novos':quant_numeros_novos,
                                               'quant_numeros_portabilidade':quant_numeros_portabilidade,
                                               'VendaMes':VendaMes,
                                               })

def ClientesVoip(request):
    clientes = ServicoVoip.objects.filter(reservado_voip='True')
    quant_clientes_ativo = ServicoVoip.objects.filter(reservado_voip='True').count()


    return render(request, 'sales/clientes-voip.html', {'clientes':clientes,
                                                        'quant_clientes_ativo':quant_clientes_ativo,
                                                        })

#------------------------------------  VALES  -------------------------------------

def ValeRefeicoes(request):
    vales_sem_valor = ValeRefeicao.objects.filter(valor_vale__isnull=True)
    vales_com_valor = ValeRefeicao.objects.filter(valor_vale__isnull=False)

    startdate = request.GET.get('startdate')
    enddate = request.GET.get('enddate')
    queryset = request.GET.get('q')
    if startdate and enddate and queryset:
        vales_com_valor = ValeRefeicao.objects.filter(Q(data_vale__range=[startdate, enddate])
                                                      & Q(nome_funcionario__icontains=queryset))

    return render(request, 'sales/vale-refeicao.html', {'vales_sem_valor': vales_sem_valor,
                                                        'vales_com_valor':vales_com_valor})



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






@login_required(login_url='/login/')
def AdicionarValorVale(request, id=None):
    vale = get_object_or_404(ValeRefeicao, id=id)
    form = AdicionarValorValeRefeicaoForm(request.POST or None, instance=vale)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Valor adicionado com sucesso.')
        return redirect('/vendas/vale-refeicao/')
    return render(request, 'sales/adicionar-valor-vale.html', {'form': form})



