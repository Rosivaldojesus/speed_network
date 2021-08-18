from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.edit import CreateView
from .models import ServicoVoip
from .forms import AdicionarNumeroVoipForm, ReservarNumeroVoipForm, FinalizarNumeroVoipForm
from django.contrib import messages

# Create your views here.
def Index(request):
    quantidade_voip_disponiveis = ServicoVoip.objects.filter(reservado_voip='False').count()
    quantidade_voip_reservados = ServicoVoip.objects.filter(reservado_voip='True').count()
    return render(request, 'voip/index.html', {'quantidade_voip_disponiveis':quantidade_voip_disponiveis,
                                               'quantidade_voip_reservados':quantidade_voip_reservados})


class AdicionarNumeroVoip(CreateView):
    model = ServicoVoip
    form_class = AdicionarNumeroVoipForm
    success_url = '/voip/'
    template_name = 'voip/adicionar-numero-voip.html'

def ListaVoipDisponiveis(request):
    voip_disponiveis = ServicoVoip.objects.filter(reservado_voip='False')
    return render(request, 'voip/lista-voip-disponiveis.html', {'voip_disponiveis': voip_disponiveis})

def ListaVoipReservados(request):
    voip_reservados = ServicoVoip.objects.filter(reservado_voip='True')
    return render(request, 'voip/lista-voip-reservados.html', {'voip_reservados': voip_reservados})

def ListaVoipFinalizados(request):
    voip_finalizados = ServicoVoip.objects.filter(reservado_voip='True').filter(finalizado_voip='True')
    return render(request, 'voip/lista-voip-finalizados.html', {'voip_finalizados': voip_finalizados})


def VoipVisualizar(request):
    voip = request.GET.get('id')
    if voip:
        voip = ServicoVoip.objects.get(id=voip)
    return render(request, 'voip/visualizar-voip-finalizados.html', {'voip': voip})


def ReservarNumeroVoip(request, id=None):
    numero_voip = get_object_or_404(ServicoVoip, id=id)
    form = ReservarNumeroVoipForm(request.POST or None, instance=numero_voip)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.reservado_voip = 'True'
        obj = form.save()
        obj.save()
        messages.success(request, 'Número reservado para o cliente!')
        return redirect('/voip/')
    return render(request, 'voip/reservar-numero-voip.html', {'form': form})


def FinalizarNumeroVoip(request, id=None):
    numero_voip = get_object_or_404(ServicoVoip, id=id)
    form = FinalizarNumeroVoipForm(request.POST or None, instance=numero_voip)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.finalizado_voip = 'True'
        obj = form.save()
        obj.save()
        messages.success(request, 'Número finalizado com sucesso!')
        return redirect('/voip/')
    return render(request, 'voip/finalizar-numero-voip.html', {'form': form, 'numero_voip':numero_voip})

