from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from ..sales.models import Instalacao
from ..services.models import Servico
from ..core.models import Manuais, SenhasEquipamentos

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


    return render(request, 'core/index.html',{'pendentes':pendentes,

                                            'quant_servico_aberto': quant_servico_aberto,
                                              'quant_servico_agendado': quant_servico_agendado,
                                              'quant_servico_finalizados': quant_servico_finalizados,

                                              'quant_instalacao_aberta': quant_instalacao_aberta,
                                              'quant_instalacao_agendada':quant_instalacao_agendada,
                                              'quant_instalacao_concluida':quant_instalacao_concluida,



                                              })

def ManuaisServicos(request):
    manuais = Manuais.objects.all()
    queryset = request.GET.get('q')
    if queryset:
        manuais = Manuais.objects.filter(
            Q(nome_manual__icontaians=queryset)
        )
    return render(request, 'core/manuais.html', {'manuais':manuais})


def Senhas(request):
    senhas = SenhasEquipamentos.objects.all()
    return render(request, 'core/senhas.html', {'senhas': senhas})