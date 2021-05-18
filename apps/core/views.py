from select import select

from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from django.shortcuts import render
from ..sales.models import Instalacao
from ..services.models import Servico
from ..core.models import Manuais, SenhasEquipamentos, SenhasPorEquipamentos


from django.db.models import Count


# Create your views here.
def login(request):
    return render(request, 'login.html')





#@login_required(login_url='/login/')
def Index(request):
    pendentes = Instalacao.objects.all().count()
    quant_servico_aberto = Servico.objects.filter(status_agendado='False').filter(status_concluido='False').count()
    quant_servico_agendado = Servico.objects.filter(status_agendado='True').filter(status_concluido='False').count()
    quant_servico_finalizados = Servico.objects.all().filter(status_concluido='True').count()

    quant_instalacao_aberta = Instalacao.objects.filter(status_agendada='False').filter(concluido='False').count()
    quant_instalacao_agendada = Instalacao.objects.filter(status_agendada='True').filter(concluido='False').count()
    quant_instalacao_concluida = Instalacao.objects.filter(concluido='True').count()




    data = Instalacao.objects.filter(concluido='True').values('data_finalizacao').annotate(number=Count('id'))[:7]
    #data =  Order.objects.filter().extra({'day':"Extract(day from created)"}).values_list('day').annotate(Count('id'))



    return render(request, 'core/index.html',{'pendentes':pendentes,

                                            'quant_servico_aberto': quant_servico_aberto,
                                              'quant_servico_agendado': quant_servico_agendado,
                                              'quant_servico_finalizados': quant_servico_finalizados,

                                              'quant_instalacao_aberta': quant_instalacao_aberta,
                                              'quant_instalacao_agendada':quant_instalacao_agendada,
                                              'quant_instalacao_concluida':quant_instalacao_concluida,

                                              'data': data



                                              })

def ManuaisServicos(request):
    manuais = Manuais.objects.all()
    queryset = request.GET.get('q')
    if queryset:
        manuais = Manuais.objects.filter(
            Q(nome_manual__icontaians=queryset)
        )
    return render(request, 'core/manuais.html', {'manuais':manuais})


def ManuaisVisualizacao(request):
    manual = request.GET.get('id')
    if manual:
        manual = Manuais.objects.get(id=manual)
    return render(request, 'core/manuais-visualizacao.html',{'manual': manual})


def Senhas(request):
    senhas = SenhasEquipamentos.objects.all()
    return render(request, 'core/senhas.html', {'senhas': senhas})


def SenhasPorEquipamento(request):
    senhasPorEquipamentos = SenhasPorEquipamentos.objects.all().order_by('codigo_equipamento')
    queryset = request.GET.get('q')
    if queryset:
        senhasPorEquipamentos = SenhasPorEquipamentos.objects.filter(
            Q(codigo_equipamento__icontains=queryset) |
            Q(sn_equipamento__icontains=queryset)
        )
    return render(request, 'core/senhas-por-equipamento.html', {'senhasPorEquipamentos': senhasPorEquipamentos})