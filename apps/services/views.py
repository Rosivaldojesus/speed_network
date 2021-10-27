from datetime import datetime, date
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ServicoForm, AgendarServicoForm, EditarAgendarServicoForm,\
    FinalizarServicoForm, ReservarVoipPortabilidadeForm
from .forms import ReservarVoipForm
from .models import Servico, ServicoVoip
from django.db.models import Q, Sum, Count
from django.views.generic.edit import CreateView
from django.db.models.functions import TruncMonth


# Create your views here.
def Index(request):
    contarAbertos = Servico.objects.all().filter().filter(status_agendado='False')\
    .filter(status_concluido='False').count()
    contarAgendados = Servico.objects.filter(status_agendado='True')\
    .filter(status_concluido='False').count()
    contarFinalizados = Servico.objects.all().filter(status_concluido='True').count()
    diarios = Servico.objects.all().filter(status_concluido='True').values('data_finalizacao').annotate(number=Count('contato_servico'))
   # diarioInstalaçao = Instalacao.objects.filter(concluido='True').values('data_finalizacao').annotate( number=Count('data_finalizacao')).order_by('data_finalizacao')[90:]
    servicosMensal = Servico.objects.annotate(month=TruncMonth('data_finalizacao')).filter(status_concluido='True').values('month').annotate(c=Count('data_finalizacao')).values('month', 'c').order_by('month')

    diarioServicos = Servico.objects.filter(status_concluido='True').values('data_finalizacao').annotate(number=Count('data_finalizacao')).order_by('data_finalizacao')[90:]



    return render(request, 'services/index.html', {'contarAbertos': contarAbertos,
                                                   'contarFinalizados': contarFinalizados,
                                                   'contarAgendados': contarAgendados,
                                                    'diarios': diarios,
                                                   'servicosMensal': servicosMensal,
                                                   'diarioServicos': diarioServicos,
                                                   })

def CadastroServico(request):
    form = ServicoForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.criado_por = request.user
        obj = form.save()
        obj.save()
        messages.success(request, 'Serviço adicionado com sucesso!')
        return redirect('/servicos/')
    else:
        form = ServicoForm()
    return render(request, 'services/cadastro-servico.html', {'form': form})


def EditarServico(request, id=None):
    editar = get_object_or_404(Servico, id=id)
    form = ServicoForm(request.POST or None, instance=editar)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Serviço editado com sucesso!')
        return redirect('/servicos/servicos-abertos/')
    return render(request, 'services/editar-servico.html', {'form': form})


def RemoverServico(request, id=None):
    servico = get_object_or_404(Servico, id=id)
    if request.method == "POST":
        servico.delete()
        messages.success(request, 'Serviço removido com sucesso!')
        return redirect('/servicos/')
    return render(request, 'services/deletar-servico.html', {'servoco': servico})


def ServicosAbertos(request):
    abertos = Servico.objects.order_by('-id')\
        .filter(status_agendado='False')\
        .filter(status_concluido='False')
    qquant_aberto = Servico.objects.filter(status_agendado='False').filter(status_concluido='False').count()
    return render(request, 'services/servicos-abertos.html', {'abertos':abertos,
                                                              'qquant_aberto':qquant_aberto
                                                              })


def EditarServicoAgendado(request, id=None):
    editarAgendado = get_object_or_404(Servico, id=id)
    form = EditarAgendarServicoForm(request.POST or None, instance=editarAgendado)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Serviço agendado, editado com sucesso!')
        return redirect('/servicos/')
    return render(request, 'services/editar-servico.html', {'form':form})



def ServicosAgendados(request):
    today = date.today()
    agendados = Servico.objects.filter(status_agendado='True').filter(status_concluido='False').\
        order_by('data_agendada','hora_agendada')
    quant_agendados = Servico.objects.filter(status_agendado='True').filter(status_concluido='False').count()
    queryset = request.GET.get('q')
    startdate = request.GET.get('date')
    if queryset:
        agendados = Servico.objects.filter(
            Q(contato_servico=queryset) |
            Q(data_agendada__icontains=startdate)).filter(status_concluido='False')
        quant_agendados = Servico.objects.filter(
            Q(contato_servico=queryset) |
            Q(data_agendada__icontains=startdate)).filter(status_concluido='False').count()
    if startdate:
        agendados = Servico.objects.filter(Q(data_agendada__exact=startdate)).filter(status_concluido='False')
        quant_agendados = Servico.objects.filter(
            Q(contato_servico=queryset) |
            Q(data_agendada__icontains=startdate)).filter(status_concluido='False').count()
    return render(request, 'services/servicos-agendados.html', {'agendados': agendados,
                                                                'quant_agendados':quant_agendados
                                                                })

def ServicosFinalizados(request):
    finalizados = Servico.objects.filter(status_concluido='True').order_by('-id')
    queryset = request.GET.get('q')
    if queryset:
        finalizados = Servico.objects.filter(
            Q(contato_servico__icontains=queryset))
    quant_finalizados = Servico.objects.filter(status_concluido='True').count()
    return render(request, 'services/servicos-finalizados.html', {'finalizados':finalizados,
                                                                  'quant_finalizados':quant_finalizados
                                                                  })

def AgendarServico(request, id=None):
    agendar = get_object_or_404(Servico, id=id)
    form = AgendarServicoForm(request.POST or None, instance=agendar)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.agendado_por = request.user
        obj = form.save()
        obj.save()
        messages.success(request, 'Serviço agendado com sucesso!')
        return redirect('/servicos/')
    return render(request, 'services/agendar-servico.html', {'form': form})


def FinalizarServico(request, id=None):
    finalizar = get_object_or_404(Servico, id=id)
    form = FinalizarServicoForm(request.POST or None, instance=finalizar)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.finalizado_por = request.user
        obj = form.save()
        obj.save()
        messages.success(request, 'Serviço finalizado com sucesso!')
        return redirect('/servicos/')
    return render(request, 'services/finalizar-servico.html', {'form': form})


def ServicoVisualizar(request):
    servico = request.GET.get('id')
    if servico:
        servico = Servico.objects.get(id=servico)
    return render(request, 'services/visualizar-servico.html', {'servico': servico})

def DeletarServico(request, id=None):
    servico = get_object_or_404(Servico, id=id)
    if request.method == "POST":
        servico.delete()
        return redirect('/servicos/')
    return render(request, 'services/deletar-servico.html', {'servico': servico})
#-----------------------------------------------------------------------------------------------------------------------
#----------------------------------- SERVIÇOS DE VOIP ------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------



def ServicosVoip(request):
    voipDisponivel = ServicoVoip.objects.all().filter(reservado_voip='False').filter(finalizado_voip='False')
    quantDisponivel = ServicoVoip.objects.all().filter(reservado_voip='False').filter(finalizado_voip='False').count()
    voipReservado = ServicoVoip.objects.all().filter(portabilidade_voip='False').filter(reservado_voip='True')\
    .filter(finalizado_voip='False')
    voipReservadoPortabilidade = ServicoVoip.objects.all().filter(portabilidade_voip='True')\
    .filter(reservado_voip='True').filter(finalizado_voip='False')
    return render(request, 'services/servicos-voip.html', {'voipDisponivel': voipDisponivel,
                                                           'quantDisponivel': quantDisponivel,
                                                           'voipReservado': voipReservado,
                                                           'voipReservadoPortabilidade':voipReservadoPortabilidade
                                                           })

def ServicosVoipDisponiveis(request):
    voipDisponivel = ServicoVoip.objects.all().filter(finalizado_voip='False')
    return render(request, 'services/servicos-voip-disponiveis.html', {'voipDisponivel': voipDisponivel})

def ServicosVoipReservados(request):
    voipReservados = ServicoVoip.objects.all().filter(finalizado_voip='False').filter(reservado_voip='True')
    quant_Reservados = ServicoVoip.objects.all().filter(finalizado_voip='False').filter(reservado_voip='True').count()
    return render(request, 'services/servicos-voip-reservados.html', {'voipReservados': voipReservados,
                                                                      'quant_Reservados': quant_Reservados
                                                                      })

def ReservarVoip(request, id=None):
    voip = get_object_or_404(ServicoVoip, id=id)
    form = ReservarVoipForm(request.POST or None, instance=voip)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.funcionario_reserva_voip = request.user
        obj.data_reserva_voip = date.today()
        obj = form.save()
        obj.save()
        messages.success(request, 'Voip reservado com sucesso!')
        return redirect('/servicos/servicos-voip/')
    return render(request, 'services/reservar-voip.html', {'form': form})


class ReservarVoipPortabilidadeCreate(CreateView):
    model = ServicoVoip
    fields = ['nome_usuario_voip', 'cpf_usuario_voip']
    success_url = '/servicos/'




