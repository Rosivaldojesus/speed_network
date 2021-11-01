import datetime
from datetime import datetime, date
from django.db.models import Q, Count
from django.shortcuts import render, redirect,get_object_or_404
from ..sales.models import Instalacao
from ..payment.models import Pagamento
from ..services.models import Servico
from ..voip.models import ServicoVoip
from ..core.models import Manuais, SenhasEquipamentos, SenhasPorEquipamentos
from django.db.models.functions import ExtractMonth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Count, Sum
from .forms import SenhasPorEquipamentosForm
from django.http import HttpResponse
import csv

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
            messages.error(request, "Por favor, insira um usuário e senha corretos para uma conta de equipe."
             "Note que ambos campos são sensíveis a maiúsculas e minúsculas.")
    return redirect('/')


@login_required(login_url='/login/')
def Index(request):
    #Para pegar o usuário atual
    user = request.user
    #Para filtar quantidade por período
    data_atual = datetime.now()
    this_year = datetime.now().year
    last_year = datetime.now().year - 1
    this_month = date.today().month

    #------------------------------------ Query dos serviços -----------------------------------------------------------
    pendentes = Instalacao.objects.all().count()
    quant_servico_aberto = Servico.objects.filter(status_agendado='False').filter(status_concluido='False').count()
    quant_servico_agendado = Servico.objects.filter(status_agendado='True').filter(status_concluido='False').count()
    quant_servico_finalizados = Servico.objects.all().filter(status_concluido='True').count()
    quant_servicos_finalizados_mes = Servico.objects.filter(data_finalizacao__month=this_month).count()

    #------------------------------------- Query das Instalações -------------------------------------------------------
    quant_instalacao_aberta = Instalacao.objects.filter(status_agendada='False').filter(concluido='False').count()
    quant_instalacao_agendada = Instalacao.objects.filter(status_agendada='True').filter(concluido='False').count()
    quant_instalacao_concluida = Instalacao.objects.filter(concluido='True').filter(boleto_entregue='True').count()
    quant_instalacao_sem_boleto = Instalacao.objects.filter(concluido='True').filter(boleto_entregue='False').count()
    quant_instalacao_finalizados_mes = Instalacao.objects.filter(data_finalizacao__month=this_month).count()
    responsavel_instalacao = Instalacao.objects.filter(status_agendada='True').filter(concluido='False').\
        order_by('funcionario_instalacao', 'data_instalacao', 'hora_instalacao')
    hora_instalacao = Instalacao.objects.filter(status_agendada='True').filter(concluido='False').\
        values('data_instalacao').annotate(number=Count('id')).order_by('data_instalacao')
    ultimas_vendas = Instalacao.objects.filter().order_by('-id')[:6]

    #-------------------------------------- Query das Previsões de serviços e Instalaçãoes -----------------------------
    previsaoServico = Servico.objects.filter(status_agendado='True').filter(status_concluido='False').values(
        'data_agendada').annotate(number=Count('id')).order_by('data_agendada')
    previsaoInstalacao = Instalacao.objects.filter(status_agendada='True').filter(concluido='False').values(
        'data_instalacao').annotate(number=Count('id')).order_by('data_instalacao')

    # -------------------------------------- Filter service by técnico (Estudar como retirar) --------------------------
    funcionarioinstalacao = Instalacao.objects.filter(status_agendada='True').filter(concluido='False')
    instalacaoEduardo = Instalacao.objects.filter(funcionario_instalacao=12).filter(status_agendada='True').\
        filter(concluido='False').order_by('data_instalacao')
    instalacaoDiego = Instalacao.objects.filter(funcionario_instalacao=14).filter(status_agendada='True').\
        filter(concluido='False').order_by('data_instalacao')
    instalacaoPaulo = Instalacao.objects.filter(funcionario_instalacao=13).filter(status_agendada='True').\
        filter(concluido='False').order_by('data_instalacao')
    
    #---------------------------------------- Query de Serviços --------------------------------------------------------
    servicosDiarios = Servico.objects.filter(status_concluido='True').values('data_finalizacao').annotate(
        number=Count('id')).order_by('data_finalizacao')[:7]
    servicosMensais = Servico.objects.annotate(month=ExtractMonth('data_finalizacao')).values('month').annotate(
        count=Count('id')).values('month', 'count')[:7]
    instalacaoPorDia = Instalacao.objects.filter(concluido='True').values('data_finalizacao').annotate(
        number=Count('id')).order_by('data_finalizacao')[:7]
    servicoPorDia = Servico.objects.filter(status_concluido='True').values('data_finalizacao').annotate(
        number=Count('id'))[:7]

    # --------------------------------------- STATUS DE VENDAS ---------------------------------------------------------
    vendasPorVendedor = Instalacao.objects.all().values('instalacao_criado_por').annotate(
        number=Count('instalacao_criado_por'))

    #---------------------------------------- STATUS VOIP --------------------------------------------------------------
    voipDisponiveis = ServicoVoip.objects.filter(reservado_voip='False').filter(finalizado_voip='False').count()
    voipReservados = ServicoVoip.objects.filter(portabilidade_voip= 'False').filter(reservado_voip='True').\
        filter(finalizado_voip='False').count()
    voipPortabilidade = ServicoVoip.objects.filter(portabilidade_voip= 'True').filter(reservado_voip='True').\
        filter(finalizado_voip='False').count()
    #--------------------------------------- Query para Pagamentos ------------      -----------------------------------
    data_atual = datetime.now()
    pagamentos_atrasados = Pagamento.objects.filter(status_pago= 'False').filter(data_pagamento__lt=data_atual).count()
    pagamentos_para_vencer = Pagamento.objects.filter(status_pago= 'False').filter(data_pagamento__gt=data_atual).count()

    pagamentos_para_hoje = Pagamento.objects.filter(status_pago= 'False').filter(data_pagamento=data_atual).count()

    #------------------------------------------ SERVIÇOS DE VOIP -------------------------------------------------------
    # Contagem referentes ao números novos voip
    quantidade_voip_disponiveis = ServicoVoip.objects.filter(reservado_voip='False'). \
        filter(finalizado_voip='False'). \
        filter(boleto_entregue='False').count()
    quantidade_voip_reservados = ServicoVoip.objects.filter(reservado_voip='True'). \
        filter(portabilidade_voip='False'). \
        filter(finalizado_voip='False'). \
        filter(boleto_entregue='False').count()
    quantidade_voip_sem_boleto = ServicoVoip.objects.filter(reservado_voip='True'). \
        filter(finalizado_voip='True').filter(boleto_entregue='False').count()
    quantidade_voip_finalizados = ServicoVoip.objects. \
        filter(reservado_voip='True'). \
        filter(finalizado_voip='True'). \
        filter(boleto_entregue='True').count()

    # Contagem referentes ao números de portabiliade
    quantidade_portabilidade_aguardando = ServicoVoip.objects.filter(reservado_voip='True'). \
        filter(portabilidade_voip='True'). \
        filter(portabilidade_analise='False'). \
        filter(finalizado_voip='False'). \
        filter(boleto_entregue='False').count()
    quantidade_portabilidade_analise = ServicoVoip.objects.filter(reservado_voip='True'). \
        filter(portabilidade_voip='True'). \
        filter(portabilidade_analise='True'). \
        filter(finalizado_voip='False'). \
        filter(boleto_entregue='False').count()
    quantidade_portabilidade_finalizados = ServicoVoip.objects.filter(reservado_voip='True'). \
        filter(portabilidade_voip='True'). \
        filter(portabilidade_analise='True'). \
        filter(finalizado_voip='True'). \
        filter(boleto_entregue='False').count()

    return render(request, 'core/index.html',{'pendentes':pendentes,
                                              'quant_servico_aberto': quant_servico_aberto,
                                              'quant_servico_agendado': quant_servico_agendado,
                                              'quant_servico_finalizados': quant_servico_finalizados,
                                              'quant_servicos_finalizados_mes':quant_servicos_finalizados_mes,
                                              'quant_instalacao_finalizados_mes':quant_instalacao_finalizados_mes,
                                              'previsaoServico': previsaoServico,
                                              'quant_instalacao_aberta': quant_instalacao_aberta,
                                              'quant_instalacao_agendada': quant_instalacao_agendada,
                                              'quant_instalacao_concluida': quant_instalacao_concluida,
                                              'quant_instalacao_sem_boleto': quant_instalacao_sem_boleto,
                                              'responsavel_instalacao': responsavel_instalacao,
                                              'hora_instalacao':hora_instalacao,
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
                                              'voipPortabilidade':voipPortabilidade,
                                              #Últimas vendas
                                              'ultimas_vendas': ultimas_vendas,

                                              #Pagamentos
                                              'pagamentos_atrasados':pagamentos_atrasados,
                                              'pagamentos_para_vencer':pagamentos_para_vencer,
                                              'pagamentos_para_hoje':pagamentos_para_hoje,

                                              #Voips
                                              'quantidade_voip_disponiveis':quantidade_voip_disponiveis,
                                              'quantidade_voip_reservados':quantidade_voip_reservados,
                                              'quantidade_voip_sem_boleto':quantidade_voip_sem_boleto,
                                              'quantidade_voip_finalizados':quantidade_voip_finalizados,

                                              'quantidade_portabilidade_aguardando':quantidade_portabilidade_aguardando,
                                              'quantidade_portabilidade_analise':quantidade_portabilidade_analise,
                                              'quantidade_portabilidade_finalizados':quantidade_portabilidade_finalizados,
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

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
@login_required(login_url='/login/')
def Senhas(request):
    senhas = SenhasEquipamentos.objects.all()
    return render(request, 'core/senhas.html', {'senhas': senhas})


@login_required(login_url='/login/')
def SenhasPorEquipamento(request):
    senhasPorEquipamentos = SenhasPorEquipamentos.objects.all().order_by('-id')[:15]

    quant_6t = SenhasPorEquipamentos.objects.filter(equipamento=1).count()
    quant_v5 = SenhasPorEquipamentos.objects.filter(equipamento=2).count()
    quant_q2 = SenhasPorEquipamentos.objects.filter(equipamento=3).count()
    quant_nokia_140 = SenhasPorEquipamentos.objects.filter(equipamento=6).count()
    quant_nokia_240 = SenhasPorEquipamentos.objects.filter(equipamento=5).count()
    quant_modens = SenhasPorEquipamentos.objects.filter().count()

    queryset = request.GET.get('q')
    if queryset:
        senhasPorEquipamentos = SenhasPorEquipamentos.objects.filter(
            Q(
                patrimonio_equipamento__icontains=queryset
            )
        )
        
    return render(request, 'core/senhas-por-equipamento.html', {'senhasPorEquipamentos': senhasPorEquipamentos,
                                                                'quant_v5':quant_v5,
                                                                'quant_6t':quant_6t,
                                                                'quant_q2':quant_q2,
                                                                'quant_nokia_140':quant_nokia_140,
                                                                'quant_nokia_240':quant_nokia_240,
                                                                'quant_modens':quant_modens
                                                                })


def CadastroSenhasPorEquipamentos(request):
    form = SenhasPorEquipamentosForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Equipamento cadastrado com sucesso.')
        return redirect('/senhas-por-equipamento/')
    else:
        form = SenhasPorEquipamentosForm()
    return render(request, 'core/cadastro-senhas-equipamentos.html', {'form': form})


@login_required(login_url='/login/')
def EditarSenhasPorEquipamentos(request, id=None):
    senha= get_object_or_404(SenhasPorEquipamentos, id=id)
    form = SenhasPorEquipamentosForm(request.POST or None, instance=senha)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Equipamento modificado com sucesso.')
        return redirect('/senhas-por-equipamento/')
    return render(request, 'core/editar-senhas-equipamentos.html', {'form': form})


@login_required(login_url='/login/')
def InstalacoesDiarias(request):
    return render(request, 'instalacoes-diarias.html')


#Exportando os dados para CSV
def ExportarSenhasCSV(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="lista-senhas.csv"'

    senhas = SenhasPorEquipamentos.objects.all()

    writer = csv.writer(response)
    writer.writerow(['codigo_equipamento', 'sn_equipamento', 'equipamento', 'ip_equipamento', 'login',
                     'senha', 'fabricante', 'patrimonio_equipamento', 'data_cadastro'])
    for senha in senhas:
        writer.writerow([senha.codigo_equipamento, senha.sn_equipamento, senha.equipamento, senha.ip_equipamento,
                         senha.login, senha.senha, senha.fabricante, senha.patrimonio_equipamento, senha.data_cadastro,
                         ])
    return response