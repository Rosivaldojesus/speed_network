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

import plotly.graph_objs as go
from plotly.offline import plot


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

    diarioServicos = Servico.objects.filter(status_concluido='True').values('data_finalizacao').annotate(number=Count('data_finalizacao')).order_by('data_finalizacao')[150:]

    #Quantidade de serviços por categoria

    quant_outros = Servico.objects.filter(categoria=2).count()
    quant_serv_velocidade = Servico.objects.filter(categoria=3).count()
    quant_serv_osciliacao = Servico.objects.filter(categoria=4).count()
    quant_serv_retirada = Servico.objects.filter(categoria=5).count()
    quant_serv_fibra_rompida = Servico.objects.filter(categoria=6).count()
    quant_serv_troca_modem = Servico.objects.filter(categoria=7).count()
    quant_serv_voip = Servico.objects.filter(categoria=8).count()
    quant_serv_sinal_alto = Servico.objects.filter(categoria=9).count()
    quant_trocar_senha = Servico.objects.filter(categoria=10).count()


    fig = go.Figure()
    scatter = go.Scatter(x=["Segunda", 'Terça', 'Quarta', 'Quinta'], y=[0, 10, 17, 8],
                         mode='lines', name='test',
                         opacity=0.8, marker_color='green'
                         )
    fig.add_trace(scatter)
    graph = plot(fig, output_type='div')




    context = {
        'graph': graph,

        'contarAbertos': contarAbertos,
        'contarFinalizados': contarFinalizados,
        'contarAgendados': contarAgendados,
        'diarios': diarios,
        'servicosMensal': servicosMensal,
        'diarioServicos': diarioServicos,
        #Quantidade de serviços por categorias
        'quant_serv_velocidade': quant_serv_velocidade,
        'quant_serv_osciliacao': quant_serv_osciliacao,
        'quant_serv_retirada': quant_serv_retirada,
        'quant_serv_fibra_rompida': quant_serv_fibra_rompida,
        'quant_serv_troca_modem': quant_serv_troca_modem,
        'quant_serv_voip': quant_serv_voip,
        'quant_serv_sinal_alto': quant_serv_sinal_alto,
        'quant_outros': quant_outros,
        'quant_trocar_senha': quant_trocar_senha
    }

    return render(request, 'services/index.html', context)

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




