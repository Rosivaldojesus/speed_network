import datetime
from datetime import datetime, date
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from ..sales.models import Instalacao
from ..payment.models import Pagamento
from ..services.models import Servico
from ..voip.models import ServicoVoip
from ..core.models import Manuais, SenhasEquipamentos, SenhasPorEquipamentos
from django.db.models.functions import ExtractMonth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Count
from .forms import SenhasPorEquipamentosForm
from django.http import HttpResponse
import csv
from .forms import UserForm
from django.db import connection


# Create your views here.
def add_user(request):
    template_name = 'core/add-user.html'
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.set_password(f.password)
            f.save()
            messages.success(request, 'Usuário criado com sucesso!!!')
            return redirect('/novo-usuario/')
        context['form'] = form
    else:
        form = UserForm()
    context['form'] = form
    return render(request, template_name, context)


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
    this_month = date.today().month
    #this_month = datetime.now().month
    data_atual = datetime.now()

   

    #  ------------------------------------ Query dos serviços --------------------------------------------------------
    pendentes = Instalacao.objects.all().count()
    quant_servico_aberto = Servico.objects.filter(status_agendado='False', status_concluido='False').count()
    quant_servico_agendado = Servico.objects.filter(status_agendado='True', status_concluido='False').count()
    quant_servico_finalizados = Servico.objects.filter(status_concluido='True').count()

    quant_servicos_finalizados_mes = Servico.objects.filter(data_finalizacao__month=this_month).count()

    #  ---------------------------------- Query das Instalações -------------------------------------------------------
    quant_instalacao_aberta = Instalacao.objects.filter(status_agendada='False', concluido='False').count()
    quant_instalacao_agendada = Instalacao.objects.filter(status_agendada='True', concluido='False').count()
    quant_instalacao_concluida = Instalacao.objects.filter(concluido='True', boleto_entregue='True').count()
    quant_instalacao_sem_boleto = Instalacao.objects.filter(concluido='True', boleto_entregue='False').count()

    quant_instalacao_finalizados_mes = Instalacao.objects.filter(data_finalizacao__month=this_month).count()

    responsavel_instalacao = Instalacao.objects.filter(status_agendada='True', concluido='False').\
        order_by('funcionario_instalacao', 'data_instalacao', 'hora_instalacao')
    hora_instalacao = Instalacao.objects.filter(status_agendada='True', concluido='False').\
        values('data_instalacao').annotate(number=Count('id')).order_by('data_instalacao')
    ultimas_vendas = Instalacao.objects.order_by('-id')[:6]

    #  ----------------------------------- Query das Previsões de serviços e Instalaçãoes -----------------------------
    previsaoServico = Servico.objects.filter(status_agendado='True', status_concluido='False').values(
        'data_agendada').annotate(number=Count('id')).order_by('data_agendada')
    previsaoInstalacao = Instalacao.objects.filter(status_agendada='True', concluido='False').values(
        'data_instalacao').annotate(number=Count('id')).order_by('data_instalacao')

    # ------->>>> Filter service by técnico (Estudar como retirar)
    #  ------------------------------------ Filter service by técnico (Estudar como retirar) --------------------------
    funcionarioinstalacao = Instalacao.objects.filter(status_agendada='True', concluido='False')
    instalacaoEduardo = Instalacao.objects.filter(funcionario_instalacao=12, status_agendada='True').\
        filter(concluido='False').order_by('data_instalacao')
    instalacaoDiego = Instalacao.objects.filter(funcionario_instalacao=14, status_agendada='True').\
        filter(concluido='False').order_by('data_instalacao')
    instalacaoPaulo = Instalacao.objects.filter(funcionario_instalacao=13, status_agendada='True').\
        filter(concluido='False').order_by('data_instalacao')
    
    #  ------------------------------------- Query de Serviços --------------------------------------------------------
    servicosDiarios = Servico.objects.filter(status_concluido='True').values('data_finalizacao').annotate(
        number=Count('id')).order_by('data_finalizacao')[:7]
    servicosMensais = Servico.objects.annotate(month=ExtractMonth('data_finalizacao')).values('month').annotate(
        count=Count('id')).values('month', 'count')[:7]
    instalacaoPorDia = Instalacao.objects.filter(concluido='True').values('data_finalizacao').annotate(
        number=Count('id')).order_by('data_finalizacao')[:7]
    servicoPorDia = Servico.objects.filter(status_concluido='True').values('data_finalizacao').annotate(
        number=Count('id'))[:7]

    #  ------------------------------------- STATUS DE VENDAS ---------------------------------------------------------
    vendasPorVendedor = Instalacao.objects.all().values('instalacao_criado_por').\
        annotate(number=Count('instalacao_criado_por'))

    #  ------------------------------------- STATUS VOIP --------------------------------------------------------------
    voipDisponiveis = ServicoVoip.objects.filter(reservado_voip='False', finalizado_voip='False').count()
    voipReservados = ServicoVoip.objects.filter(portabilidade_voip='False', reservado_voip='True', finalizado_voip='False').count()
    voipPortabilidade = ServicoVoip.objects.filter(portabilidade_voip='True', reservado_voip='True', finalizado_voip='False').count()
    #  ------------------------------------ Query para Pagamentos ------------      -----------------------------------
    
    pagamentos_atrasados = Pagamento.objects.filter(status_pago='False', data_pagamento__lt=data_atual).count()
    pagamentos_para_vencer = Pagamento.objects.filter(status_pago='False', data_pagamento__gt=data_atual).count()
    pagamentos_para_hoje = Pagamento.objects.filter(status_pago='False', data_pagamento=data_atual).count()

    #  --------------------------------------- SERVIÇOS DE VOIP -------------------------------------------------------
    # Contagem referentes ao números novos voip
    quantidade_voip_disponiveis = ServicoVoip.objects.filter(
        reservado_voip='False', finalizado_voip='False',boleto_entregue='False').count()
    quantidade_voip_reservados = ServicoVoip.objects.filter(
        reservado_voip='True', portabilidade_voip='False', finalizado_voip='False', boleto_entregue='False' ).count()
    quantidade_voip_sem_boleto = ServicoVoip.objects.filter(
        reservado_voip='True', finalizado_voip='True', boleto_entregue='False').count()
    quantidade_voip_finalizados = ServicoVoip.objects.filter(
        reservado_voip='True', finalizado_voip='True', boleto_entregue='True' ).count()

    #  Contagem referentes ao números de portabilidade
    quantidade_portabilidade_aguardando = ServicoVoip.objects.filter(
        reservado_voip='True', portabilidade_voip='True', portabilidade_analise='False', finalizado_voip='False',
        boleto_entregue='False').count()

    quantidade_portabilidade_analise = ServicoVoip.objects.filter(
        reservado_voip='True', portabilidade_voip='True', portabilidade_analise='True', finalizado_voip='False', 
        boleto_entregue='False'  ).count()

    quantidade_portabilidade_finalizados = ServicoVoip.objects.filter(
        reservado_voip='True', portabilidade_voip='True', portabilidade_analise='True', finalizado_voip='True',
         boleto_entregue='False').count()

    context = {
        'pendentes': pendentes,
        'quant_servico_aberto': quant_servico_aberto,
        'quant_servico_agendado': quant_servico_agendado,
        'quant_servico_finalizados': quant_servico_finalizados,
        'quant_servicos_finalizados_mes': quant_servicos_finalizados_mes,
        'quant_instalacao_finalizados_mes': quant_instalacao_finalizados_mes,
        'previsaoServico': previsaoServico,
        'quant_instalacao_aberta': quant_instalacao_aberta,
        'quant_instalacao_agendada': quant_instalacao_agendada,
        'quant_instalacao_concluida': quant_instalacao_concluida,
        'quant_instalacao_sem_boleto': quant_instalacao_sem_boleto,
        'responsavel_instalacao': responsavel_instalacao,
        'hora_instalacao': hora_instalacao,
        'funcionarioinstalacao': funcionarioinstalacao,
        'instalacaoEduardo': instalacaoEduardo,
        'instalacaoDiego': instalacaoDiego,
        'instalacaoPaulo': instalacaoPaulo,
        'previsaoInstalacao': previsaoInstalacao,
        'instalacaoPorDia': instalacaoPorDia,
        'servicoPorDia': servicoPorDia,
        'servicosDiarios': servicosDiarios,
        'servicosMensais': servicosMensais,
        # Status Vendas
        'vendasPorVendedor': vendasPorVendedor,
        # Status Voip
        'voipDisponiveis': voipDisponiveis,
        'voipReservados': voipReservados,
        'voipPortabilidade': voipPortabilidade,
        # Últimas vendas
        'ultimas_vendas': ultimas_vendas,

        # Pagamentos
        'pagamentos_atrasados': pagamentos_atrasados,
        'pagamentos_para_vencer': pagamentos_para_vencer,
        'pagamentos_para_hoje': pagamentos_para_hoje,

        # Voips
        'quantidade_voip_disponiveis': quantidade_voip_disponiveis,
        'quantidade_voip_reservados': quantidade_voip_reservados,
        'quantidade_voip_sem_boleto': quantidade_voip_sem_boleto,
        'quantidade_voip_finalizados': quantidade_voip_finalizados,

        'quantidade_portabilidade_aguardando': quantidade_portabilidade_aguardando,
        'quantidade_portabilidade_analise': quantidade_portabilidade_analise,
        'quantidade_portabilidade_finalizados': quantidade_portabilidade_finalizados,
    }
    return render(request, 'core/index.html', context)


@login_required(login_url='/login/')
def ManuaisServicos(request):
    manuais = Manuais.objects.all()
    queryset = request.GET.get('q')
    if queryset:
        manuais = Manuais.objects.filter(
            Q(nome_manual__icontaians=queryset)
        )
    context = {
        'manuais': manuais
    }
    return render(request, 'core/manuais.html', context)


@login_required(login_url='/login/')
def ManuaisVisualizacao(request):
    manual = request.GET.get('id')
    if manual:
        manual = Manuais.objects.get(id=manual)
    context = {
        'manual': manual
    }
    return render(request, 'core/manuais-visualizacao.html', context)


#  ---------------------------------------------------------------------------------------------------------------------


@login_required(login_url='/login/')
def Senhas(request):
    senhas = SenhasEquipamentos.objects.all()
    return render(request, 'core/senhas.html', {'senhas': senhas})


@login_required(login_url='/login/')
def SenhasPorEquipamento(request):
    senhasPorEquipamentos = SenhasPorEquipamentos.objects.select_related('equipamento', 'fabricante').order_by('-id')[:15]

    quant_6t = SenhasPorEquipamentos.objects.filter(equipamento=1).count()
    quant_v5 = SenhasPorEquipamentos.objects.filter(equipamento=2).count()
    quant_q2 = SenhasPorEquipamentos.objects.filter(equipamento=3).count()
    quant_nokia_140 = SenhasPorEquipamentos.objects.filter(equipamento=6).count()
    quant_nokia_240 = SenhasPorEquipamentos.objects.filter(equipamento=5).count()
    quant_nokia_2425A = SenhasPorEquipamentos.objects.filter(equipamento=7).count()
    quant_nokia_1425A = SenhasPorEquipamentos.objects.filter(equipamento=8).count()
    quant_modens = SenhasPorEquipamentos.objects.filter().count()

    queryset = request.GET.get('q')
    patrimonio = request.GET.get('p')

    if queryset:
        senhasPorEquipamentos = SenhasPorEquipamentos.objects.\
            filter(Q(codigo_equipamento__icontains=queryset) | Q(sn_equipamento__icontains=queryset))

    elif patrimonio:
        senhasPorEquipamentos = SenhasPorEquipamentos.objects.filter(Q(patrimonio_equipamento__exact=patrimonio))

    query = connection.queries
    queries = len(query)

    context = {
        'senhasPorEquipamentos': senhasPorEquipamentos,
        'quant_v5': quant_v5,
        'quant_6t': quant_6t,
        'quant_q2': quant_q2,
        'quant_nokia_140': quant_nokia_140,
        'quant_nokia_240': quant_nokia_240,
        'quant_nokia_2425A': quant_nokia_2425A,
        'quant_nokia_1425A': quant_nokia_1425A,
        'quant_modens': quant_modens,

        'queries': queries,
        'query': query,
    }
    return render(request, 'core/senhas-por-equipamento.html', context)


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
    senha = get_object_or_404(SenhasPorEquipamentos, id=id)
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


#  Exportando os dados para CSV
def ExportarSenhasCSV(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="lista-senhas.csv"'

    senhas = SenhasPorEquipamentos.objects.all()

    writer = csv.writer(response)
    writer.writerow(
        [
            'codigo_equipamento', 'sn_equipamento', 'equipamento', 'ip_equipamento', 'login', 'senha', 'fabricante',
            'patrimonio_equipamento', 'data_cadastro'
        ]
    )
    for senha in senhas:
        writer.writerow(
            [
                senha.codigo_equipamento, senha.sn_equipamento, senha.equipamento, senha.ip_equipamento, senha.login,
                senha.senha, senha.fabricante, senha.patrimonio_equipamento, senha.data_cadastro,
            ]
        )
    return response
