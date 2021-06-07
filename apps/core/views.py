from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q, Count
from django.shortcuts import render, redirect
from ..sales.models import Instalacao
from ..services.models import Servico, ServicoVoip
from ..core.models import Manuais, SenhasEquipamentos, SenhasPorEquipamentos
from django.db.models.functions import ExtractMonth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


from django.db.models import Count, Sum


# Create your views here.
def login_user(request):
    return render(request, 'core/login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Por favor, insira um usuário e senha corretos "
                                    "para uma conta de equipe. Note que ambos campos"
                                    " são sensíveis a maiúsculas e minúsculas.")

    return redirect('/')

@login_required(login_url='/login/')
def Index(request):
    user = request.user
    pendentes = Instalacao.objects.all().count()
    quant_servico_aberto = Servico.objects.filter(status_agendado='False').filter(status_concluido='False').count()
    quant_servico_agendado = Servico.objects.filter(status_agendado='True').filter(status_concluido='False').count()
    quant_servico_finalizados = Servico.objects.all().filter(status_concluido='True').count()

    quant_servico_finalizados_mes = Servico.objects.annotate(month=ExtractMonth('data_finalizacao')).values(
        'month').annotate(count=Count('data_finalizacao'))

    previsaoServico = Servico.objects.filter(status_agendado='True').filter(status_concluido='False').values('data_agendada').annotate(number=Count('id')).order_by('data_agendada')


    quant_instalacao_aberta = Instalacao.objects.filter(status_agendada='False').filter(concluido='False').count()
    quant_instalacao_agendada = Instalacao.objects.filter(status_agendada='True').filter(concluido='False').count()
    quant_instalacao_concluida = Instalacao.objects.filter(concluido='True').filter(boleto_entregue='True').count()
    quant_instalacao_sem_boleto = Instalacao.objects.filter(concluido='True').filter(boleto_entregue='False').count()
    quant_instalacao_finalizados_mes = Instalacao.objects.annotate(month=ExtractMonth('data_concluido')).values(
        'month').annotate(count=Count('data_concluido'))
    previsaoInstalacao = Instalacao.objects.filter(status_agendada='True').filter(concluido='False').values('data_instalacao').annotate(number=Count('id')).order_by('data_instalacao')
    funcionarioinstalacao = Instalacao.objects.filter(status_agendada='True').filter(concluido='False')


    instalacaoEduardo = Instalacao.objects.filter(funcionario_instalacao=12).filter(status_agendada='True').filter(concluido='False').order_by('data_instalacao')
    instalacaoDiego = Instalacao.objects.filter(funcionario_instalacao=14).filter(status_agendada='True').filter(concluido='False').order_by('data_instalacao')
    instalacaoPaulo = Instalacao.objects.filter(funcionario_instalacao=13).filter(status_agendada='True').filter(concluido='False').order_by('data_instalacao')


    servicosDiarios = Servico.objects.filter(status_concluido='True').values('data_finalizacao')\
                          .annotate(number=Count('id')).order_by('data_finalizacao')[:7]
    servicosMensais = Servico.objects.annotate(month=ExtractMonth('data_finalizacao')).values('month').annotate(
        count=Count('id')).values('month', 'count')[:7]

    instalacaoPorDia = Instalacao.objects.filter(concluido='True').values('data_finalizacao').annotate(number=Count('id')).order_by('data_finalizacao')[:7]
    servicoPorDia = Servico.objects.filter(status_concluido='True').values('data_finalizacao').annotate(number=Count('id'))[:7]

    #STATUS DE VENDAS
    vendasPorVendedor = Instalacao.objects.all().values('instalacao_criado_por').annotate(number=Count('instalacao_criado_por'))

    #STATUS VOIP
    voipDisponiveis = ServicoVoip.objects.filter(reservado_voip='False').filter(finalizado_voip='False').count()
    voipReservados = ServicoVoip.objects.filter(reservado_voip='True').filter(finalizado_voip='False').count()

    return render(request, 'core/index.html',{'pendentes':pendentes,
                                            'quant_servico_aberto': quant_servico_aberto,
                                            'quant_servico_agendado': quant_servico_agendado,
                                            'quant_servico_finalizados': quant_servico_finalizados,
                                              'quant_servico_finalizados_mes':quant_servico_finalizados_mes,
                                              'previsaoServico': previsaoServico,

                                              'quant_instalacao_aberta': quant_instalacao_aberta,
                                              'quant_instalacao_agendada': quant_instalacao_agendada,
                                              'quant_instalacao_concluida': quant_instalacao_concluida,
                                              'quant_instalacao_sem_boleto': quant_instalacao_sem_boleto,
                                              'quant_instalacao_finalizados_mes': quant_instalacao_finalizados_mes,
                                              'funcionarioinstalacao': funcionarioinstalacao,
                                              'instalacaoEduardo': instalacaoEduardo,
                                              'instalacaoDiego': instalacaoDiego,
                                              'instalacaoPaulo':instalacaoPaulo,

                                              'previsaoInstalacao': previsaoInstalacao,

                                              'instalacaoPorDia': instalacaoPorDia,
                                              'servicoPorDia': servicoPorDia,

                                              'servicosDiarios':servicosDiarios,
                                              'servicosMensais':servicosMensais,

                                              #Status Vendas
                                              'vendasPorVendedor':vendasPorVendedor,

                                              #Status Voip
                                              'voipDisponiveis':voipDisponiveis,
                                              'voipReservados':voipReservados,

                                              })

@login_required(login_url='/login/')
def ManuaisServicos(request):
    manuais = Manuais.objects.all()
    queryset = request.GET.get('q')
    if queryset:
        manuais = Manuais.objects.filter(
            Q(nome_manual__icontaians=queryset)
        )
    return render(request, 'core/manuais.html', {'manuais':manuais})


@login_required(login_url='/login/')
def ManuaisVisualizacao(request):
    manual = request.GET.get('id')
    if manual:
        manual = Manuais.objects.get(id=manual)
    return render(request, 'core/manuais-visualizacao.html',{'manual': manual})


@login_required(login_url='/login/')
def Senhas(request):
    senhas = SenhasEquipamentos.objects.all()
    return render(request, 'core/senhas.html', {'senhas': senhas})


@login_required(login_url='/login/')
def SenhasPorEquipamento(request):
    senhasPorEquipamentos = SenhasPorEquipamentos.objects.all().order_by('codigo_equipamento')[:2]
    queryset = request.GET.get('q')
    if queryset:
        senhasPorEquipamentos = SenhasPorEquipamentos.objects.filter(
            Q(codigo_equipamento__icontains=queryset) |
            Q(sn_equipamento__icontains=queryset)
        )
    return render(request, 'core/senhas-por-equipamento.html', {'senhasPorEquipamentos': senhasPorEquipamentos})


#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
@login_required(login_url='/login/')
def InstalacoesDiarias(request):
    return render(request, 'instalacoes-diarias.html')
