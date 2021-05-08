from django.shortcuts import render, redirect, get_object_or_404
from .forms import ServicoForm, AgendarServicoForm, EditarAgendarServicoForm, FinalizarServicoForm

from .models import Servico

# Create your views here.

def Index(request):
    contarAbertos = Servico.objects.all().filter().filter(status_agendado='False').filter(status_concluido='False').count()
    contarAgendados = Servico.objects.filter(status_agendado='True').filter(status_concluido='False').count()
    contarFinalizados = Servico.objects.all().filter(status_concluido='True').count()
    return render(request, 'services/index.html', {'contarAbertos': contarAbertos,
                                                   'contarFinalizados': contarFinalizados,
                                                   'contarAgendados': contarAgendados})

def CadastroServico(request):
    form = ServicoForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        return redirect('/servicos/servicos-abertos/')
    else:
        form = ServicoForm()
    return render(request, 'services/cadastro-servico.html', {'form': form})


def EditarServico(request, id=None):
    editar = get_object_or_404(Servico, id=id)
    form = ServicoForm(request.POST or None, instance=editar)
    if form.is_valid():
        obj = form.save()
        obj.save()
        return redirect('/servicos/servicos-abertos/')
    return render(request, 'services/editar-servico.html', {'form': form})

def RemoverServico(request, id=None):
    servico = get_object_or_404(Servico, id=id)
    if request.method == "POST":
        servico.delete()
        return redirect('/servicos/')
    return render(request, 'services/remover-servico.html', {'servoco': servico})




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
        return redirect('/servicos/')
    return render(request, 'services/editar-servico.html', {'form':form})


def ServicosAgendados(request):
    agendados = Servico.objects.filter(status_agendado='True').filter(status_concluido='False')
    quant_agendados = Servico.objects.filter(status_agendado='True').filter(status_concluido='False').count()
    return render(request, 'services/servicos-agendados.html', {'agendados': agendados,
                                                                'quant_agendados':quant_agendados})


def ServicosFinalizados(request):
    finalizados = Servico.objects.filter(status_concluido='True').order_by('-id')
    quant_finalizados = Servico.objects.filter(status_concluido='True').count()
    return render(request, 'services/servicos-finalizados.html', {'finalizados':finalizados,
                                                                  'quant_finalizados':quant_finalizados})


def AgendarServico(request, id=None):
    agendar = get_object_or_404(Servico, id=id)
    form = AgendarServicoForm(request.POST or None, instance=agendar)
    if form.is_valid():
        obj = form.save()
        obj.save()
        return redirect('/servicos/')
    return render(request, 'services/agendar-servico.html', {'form': form})


def FinalizarServico(request, id=None):
    finalizar = get_object_or_404(Servico, id=id)
    form = FinalizarServicoForm(request.POST or None, instance=finalizar)
    if form.is_valid():
        obj = form.save()
        obj.save()
        return redirect('/servicos/')
    return render(request, 'services/finalizar-servico.html', {'form': form})


def ServicoVisualizar(request):
    servico = request.GET.get('id')
    if servico:
        servico = Servico.objects.get(id=servico)
    return render(request, 'services/visualizar-servico.html', {'servico': servico})
