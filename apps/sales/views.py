from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum, Count, Avg
from .models import Instalacao, ValeRefeicao, Cancelamentos
from ..components.models import FuncionariosParaVale
from ..services.models import ServicoVoip
from .forms import InstalacaoCreateForm, InstalacaoUpdateForm,\
    InstalacaoAgendarForm, InstalacaoFinalizarForm, BoletoEntregueForm,\
    InstalacaoDefinirTecnicoForm, EmitirValeRefeicaoForm,\
    AdicionarValorValeRefeicaoForm, AdicionarPagamentoValeRefeicaoForm, \
    CadastrarCancelamentosForm, EditarCancelamentosForm
from ..components.models import Vendedores
from django.db.models.functions import ExtractMonth
from django.db.models.functions import TruncMonth
from datetime import datetime, date, timedelta
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic.edit import UpdateView


# Create your views here.
@login_required(login_url='/login/')
def Index(request):
    this_month = date.today().month
    instalacoes = Instalacao.objects.all().order_by('data_instalacao', 'data_instalacao')
    quant_aberta = Instalacao.objects.filter(status_agendada='False').filter(concluido='False').count()
    quant_agendada = Instalacao.objects.filter(status_agendada='True').filter(concluido='False').count()
    quant_sem_boleto = Instalacao.objects.filter(concluido='True').filter(boleto_entregue='False').count()
    quant_concluida = Instalacao.objects.filter(concluido='True').filter(data_finalizacao__month=this_month).count()

    #Filtrando instalação por Vendedor
    user = request.user
    instalacaoVendedor = Instalacao.objects.filter(instalacao_criado_por=user)
    quant_aberta_vendedor = Instalacao.objects.filter(instalacao_criado_por=user).filter(status_agendada='False')\
        .filter(concluido='False').count()
    quant_agendada_vendedor = Instalacao.objects.filter(instalacao_criado_por=user).filter(status_agendada='True')\
        .filter(concluido='False').count()
    #Instalações Mensais
    instalacoesMensais = Instalacao.objects.annotate(month=ExtractMonth('data_finalizacao')).values('month').\
        annotate(count=Count('id'))
    mensalInstalacao = Instalacao.objects.annotate(month=TruncMonth('data_finalizacao')).filter(concluido='True').\
        values('month').annotate(c=Count('data_finalizacao')).values('month', 'c').order_by('month')

    diarioInstalaçao = Instalacao.objects.filter(concluido='True').\
        filter(data_finalizacao__gte=datetime.today()-timedelta(days=30)).values('data_finalizacao').\
        annotate( number=Count('data_finalizacao')).order_by('data_finalizacao')

    mediaDiarioInstalacao = Instalacao.objects.annotate(month=TruncMonth('data_finalizacao')).\
        filter(concluido='True').values('month').annotate(c=Count('data_finalizacao')).values('month', 'c').\
        order_by('month')

    # Filtros de como o cliente conheceu a empresa
    conheceu_empresa_count = Instalacao.objects.filter(como_conheceu_empresa__isnull=True).count()
    panfletos_count = Instalacao.objects.filter(Q(como_conheceu_empresa__icontains='Panfleto')).count()
    redes_sociais_count = Instalacao.objects.filter(Q(como_conheceu_empresa__icontains='Redes Socias')).count()
    site_count = Instalacao.objects.filter(Q(como_conheceu_empresa__icontains='Site')).count()
    indicacao_count = Instalacao.objects.filter(Q(como_conheceu_empresa__icontains='Indicação')).count()
    outros_count = Instalacao.objects.filter(Q(como_conheceu_empresa__icontains='Outros')).count()

    # Filtros de como o cliente conheceu a empresa mês atual
    conheceu_empresa_mes_count = Instalacao.objects.filter(data_finalizacao__month=this_month).count()
    panfletos_mes_count = Instalacao.objects.filter(Q(como_conheceu_empresa__icontains='Panfleto')).filter(data_finalizacao__month=this_month).count()
    redes_sociais_mes_count = Instalacao.objects.filter(Q(como_conheceu_empresa__icontains='Redes Socias')).filter(data_finalizacao__month=this_month).count()
    site_mes_count = Instalacao.objects.filter(Q(como_conheceu_empresa__icontains='Site')).filter(data_finalizacao__month=this_month).count()
    indicacao_mes_count = Instalacao.objects.filter(Q(como_conheceu_empresa__icontains='Indicação')).filter(data_finalizacao__month=this_month).count()
    outros_mes_count = Instalacao.objects.filter(Q(como_conheceu_empresa__icontains='Outros')).filter(data_finalizacao__month=this_month).count()

    context = {'instalacoes': instalacoes,
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
                'mediaDiarioInstalacao':mediaDiarioInstalacao,
                # Filtros de como o cliente conheceu a empresa
                'conheceu_empresa_count': conheceu_empresa_count,
                'panfletos_count':panfletos_count,
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
    return render(request, 'sales/instalacao.html', context)

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
    quant_agendada = Instalacao.objects.filter(status_agendada='True').filter(concluido='False').count()

    queryset = request.GET.get('q')
    data_dia = request.GET.get('data_dia')
    if queryset:
        agendadas = Instalacao.objects.filter(
            Q(nome_cliente__icontains=queryset)|
            Q(sobrenome_cliente__icontains=queryset)
        ).filter(status_agendada='True')\
        .filter(concluido='False').order_by('data_instalacao', 'hora_instalacao')
    
    elif data_dia:
        agendadas = Instalacao.objects.filter(Q(data_instalacao__exact=data_dia))
        quant_agendada = Instalacao.objects.filter(Q(data_instalacao__exact=data_dia)).count()

    context = {
        'agendadas':agendadas,
        'quant_agendada':quant_agendada,
    }
    
    #Filtro por vendedor
    #user = request.user
    #agendadas_vendedor = Instalacao.objects.filter(instalacao_criado_por=user).filter(status_agendada='True') \
        #.filter(concluido='False').order_by('data_instalacao', 'hora_instalacao')
    #quant_agendada_vendedor = Instalacao.objects.filter(instalacao_criado_por=user).\
        #filter(status_agendada='True').filter(concluido='False').count()
    
    return render(request, 'sales/instalacao-agendada.html', context)

@login_required(login_url='/login/')
def InstalacaoConcluida(request):
    quant_concluida = Instalacao.objects.filter(concluido='True').count()
    concluidas = Instalacao.objects.filter(concluido='True').order_by('-id')
    startdate = request.GET.get('startdate')
    queryset = request.GET.get('q')
    date = request.GET.get('date')
    if queryset:
        concluidas = Instalacao.objects.filter(Q(nome_cliente__icontains=queryset)
                                               |Q(sobrenome_cliente__icontains=queryset))

        quant_concluida = Instalacao.objects.filter(Q(nome_cliente__icontains=queryset)
                                               |Q(sobrenome_cliente__icontains=queryset)).count()
    elif date:
        concluidas = Instalacao.objects.filter(Q(data_finalizacao__exact=date))
        quant_concluida = Instalacao.objects.filter(Q(data_finalizacao__exact=date)).count()
    elif startdate:
        concluidas = Instalacao.objects.filter(Q(data_agendada__exact=startdate))

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
        concluidas = Instalacao.objects.filter(concluido='True').filter(Q(data_instalacao__range=[startdate, enddate])
                                               & Q(instalacao_vendedor__exact=queryset))
        quant_concluida = Instalacao.objects.filter(concluido='True').\
            filter(Q(data_instalacao__range=[startdate, enddate])
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

@login_required(login_url='/login/')
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
@login_required(login_url='/login/')
def Voip(request):
    VendaMes =  ServicoVoip.objects.annotate(month=TruncMonth('data_reserva_voip')).filter().values('month').annotate(c=Count('data_reserva_voip')).values('month', 'c').order_by('month')
    quant_numeros_novos = ServicoVoip.objects.filter(portabilidade_voip='False').count()
    quant_numeros_portabilidade = ServicoVoip.objects.filter(portabilidade_voip='True').count()
    return render(request, 'sales/voip.html', {'quant_numeros_novos':quant_numeros_novos,
                                               'quant_numeros_portabilidade':quant_numeros_portabilidade,
                                               'VendaMes':VendaMes,
                                               })
@login_required(login_url='/login/')
def ClientesVoip(request):
    clientes = ServicoVoip.objects.filter(reservado_voip='True')
    quant_clientes_ativo = ServicoVoip.objects.filter(reservado_voip='True').count()
    return render(request, 'sales/clientes-voip.html', {'clientes':clientes,
                                                        'quant_clientes_ativo':quant_clientes_ativo,
                                                        })

def VoipFinalizadoSemBoleto(request):
    quant_sem_boleto = ServicoVoip.objects.filter(boleto_entregue='False').count()
    concluidos = ServicoVoip.objects.all()
    return render(request, 'sales/voip-finalizado-sem-boleto.html', {'quant_sem_boleto':quant_sem_boleto,
                                                                     'concluidos':concluidos})


#------------------------------------  VALES  -------------------------------------
def ValeRefeicoes(request):
    vales_sem_valor = ValeRefeicao.objects.filter(valor_vale__isnull=True)
    vales_com_valor = ValeRefeicao.objects.filter(valor_vale__isnull=False).filter(status_pago=False)

    valor_pagar = ValeRefeicao.objects.filter(status_pago=False).filter().aggregate(Sum('valor_vale')).get('valor_vale__sum')

    startdate = request.GET.get('startdate')
    enddate = request.GET.get('enddate')
    queryset = request.GET.get('q')
    if startdate and enddate and queryset :
        vales_com_valor = ValeRefeicao.objects.filter(status_pago=False).filter(Q(data_vale__range=[startdate, enddate])
                                                      & Q(nome_funcionario__icontains=queryset))
        valor_pagar = ValeRefeicao.objects.filter(status_pago=False).filter(Q(nome_funcionario__icontains=queryset)).aggregate(Sum('valor_vale')).get('valor_vale__sum')


    elif queryset:
        vales_com_valor = ValeRefeicao.objects.filter(status_pago=False).filter(Q(nome_funcionario__icontains=queryset))
        valor_pagar = ValeRefeicao.objects.filter(status_pago=False).filter(Q(nome_funcionario__icontains=queryset)).aggregate(Sum('valor_vale')).get('valor_vale__sum')


    return render(request, 'sales/vale-refeicao.html', {'vales_sem_valor': vales_sem_valor,
                                                        'vales_com_valor': vales_com_valor,
                                                        'valor_pagar': valor_pagar,
                                                        })


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

#--------------------- Cancellations -------------------------------------------------

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




from itertools import chain
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
        context['plano_100mb_mes_atual'] = Cancelamentos.objects.filter(data__month=this_month).filter(plano_internet__icontains='69,90').count()
        context['plano_200mb_mes_atual'] = Cancelamentos.objects.filter(data__month=this_month).filter(plano_internet__icontains='89,90').count()
        context['plano_400mb_mes_atual'] = Cancelamentos.objects.filter(data__month=this_month).filter(plano_internet__icontains='99,90').count()
        context['plano_500mb_mes_atual'] = Cancelamentos.objects.filter(data__month=this_month).filter(plano_internet__icontains='119,90').count()
        context['plano_600mb_mes_atual'] = Cancelamentos.objects.filter(data__month=this_month).filter(plano_internet__icontains='149,90').count()

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




        # context.update({
        #     'mes': Cancelamentos.objects.annotate(month=TruncMonth('data')).filter().values('month').annotate(c=Count('id')).values('month', 'c').order_by('-month'),
        #     'cancelamentos': Cancelamentos.objects.all(),
        #     'count_cancelamentos': Cancelamentos.objects.all().count(),
        #
        #     # Análise por planos
        #
        #     'plano_69' : Cancelamentos.objects.filter(plano_internet='69,90').count(),
        #     'plano_89' : Cancelamentos.objects.filter(plano_internet='89,90').count(),
        #     'plano_99' : Cancelamentos.objects.filter(plano_internet='99,90').count(),
        #     'plano_119' : Cancelamentos.objects.filter(plano_internet='119,90').count(),
        #     'plano_149' : Cancelamentos.objects.filter(plano_internet='149,90').count(),
        # })


        



    #def get_queryset(self):
        #return Cancelamentos.objects.all()
    #context_object_name = 'cancelamentos'
def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            posts = Post.objects.filter(titulo_post__icontains=query)
        else:
            posts = Post.objects.filter()
        return posts







class CancelamentosUpdateView(UpdateView):
    model = Cancelamentos
    form_class = EditarCancelamentosForm
    template_name = 'sales/editar-cancelamento.html'
    template_name_suffix = 'editar-cancelamento'
    success_url = '/vendas/lista-cancelamentos/'