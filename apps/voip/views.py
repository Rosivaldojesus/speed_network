from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import ServicoVoip
from .forms import AdicionarNumeroVoipForm, ReservarNumeroVoipForm, FinalizarNumeroVoipForm,\
    SolicitarPortabilidadeVoipForm, FinalizarNumeroVoipSemBoletoForm, SolicitarNumeroVoipForm
from .forms import PortabilidadeEnviarAnaliseForm
from django.contrib import messages


# Create your views here.


def Index(request):
    quantidade_voip_disponiveis = ServicoVoip.objects.filter(reservado_voip='False').\
        filter(finalizado_voip='False').\
        filter(boleto_entregue='False').count()
    quantidade_voip_reservados = ServicoVoip.objects.filter(reservado_voip='True').\
        filter(portabilidade_voip='False').\
        filter(finalizado_voip='False').\
        filter(boleto_entregue='False').count()
    quantidade_voip_sem_boleto = ServicoVoip.objects.filter(reservado_voip='True').\
        filter(finalizado_voip='True').filter(boleto_entregue='False').count()
    quantidade_voip_finalizados = ServicoVoip.objects.\
        filter(reservado_voip='True').\
        filter(finalizado_voip='True').\
        filter(boleto_entregue='True').count()

    #  Contagem referentes ao números de portabiliade

    quantidade_portabilidade_aguardando = ServicoVoip.objects.filter(reservado_voip='True').\
        filter(portabilidade_voip='True'). \
        filter(portabilidade_analise='False').\
        filter(finalizado_voip='False').\
        filter(boleto_entregue='False').count()
    quantidade_portabilidade_analise = ServicoVoip.objects.filter(reservado_voip='True').\
        filter(portabilidade_voip='True'). \
        filter(portabilidade_analise='True').\
        filter(finalizado_voip='False').\
        filter(boleto_entregue='False').count()
    quantidade_portabilidade_finalizados = ServicoVoip.objects.filter(reservado_voip='True'). \
        filter(portabilidade_voip='True'). \
        filter(portabilidade_analise='True'). \
        filter(finalizado_voip='True'). \
        filter(boleto_entregue='False').count()

    context = {
        'quantidade_voip_disponiveis': quantidade_voip_disponiveis,
        'quantidade_voip_reservados': quantidade_voip_reservados,
        'quantidade_voip_sem_boleto': quantidade_voip_sem_boleto,
        'quantidade_voip_finalizados': quantidade_voip_finalizados,
        'quantidade_portabilidade_aguardando': quantidade_portabilidade_aguardando,
        'quantidade_portabilidade_analise': quantidade_portabilidade_analise,
        'quantidade_portabilidade_finalizados': quantidade_portabilidade_finalizados,
    }
    return render(request, 'voip/index.html', context)


class ListaClientesVoipView(TemplateView):
    model = ServicoVoip
    template_name = 'voip/lista-clientes-voip.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['lista_clientes'] = ServicoVoip.objects.filter()

        return context


class AdicionarNumeroVoip(CreateView):
    model = ServicoVoip
    form_class = AdicionarNumeroVoipForm
    success_url = '/voip/'
    template_name = 'voip/adicionar-numero-voip.html'


class SolicitarNumeroVoip(CreateView):
    model = ServicoVoip
    form_class = SolicitarNumeroVoipForm
    success_url = '/voip/'
    template_name = 'voip/solicitar-numero-voip.html'


def ListaVoipDisponiveis(request):
    voip_disponiveis = ServicoVoip.objects.filter(reservado_voip='False').filter(boleto_entregue='False').\
        filter(finalizado_voip='False')
    return render(request, 'voip/lista-voip-disponiveis.html', {'voip_disponiveis': voip_disponiveis})


def ListaVoipSolicitados(request):
    voip_solicitados = ServicoVoip.objects.filter(reservado_voip='False').filter(boleto_entregue='False').\
        filter(finalizado_voip='False')
    return render(request, 'voip/lista-voip-solicitados.html', {'voip_solicitados': voip_solicitados})


def ListaVoipReservados(request):
    voip_reservados = ServicoVoip.objects.filter(reservado_voip='True').filter(portabilidade_voip='False').\
        filter(boleto_entregue='False').filter(finalizado_voip='False')
    return render(request, 'voip/lista-voip-reservados.html', {'voip_reservados': voip_reservados})


def ListaVoipSemBoleto(request):
    voip_sem_boleto = ServicoVoip.objects.filter(reservado_voip='True').filter(finalizado_voip='True').\
        filter(boleto_entregue='False')
    return render(request, 'voip/lista-voip-sem-boleto.html', {'voip_sem_boleto': voip_sem_boleto})


def ListaVoipFinalizados(request):
    voip_finalizados = ServicoVoip.objects.filter(reservado_voip='True').filter(finalizado_voip='True').\
        filter(boleto_entregue='True')
    return render(request, 'voip/lista-voip-finalizados.html', {'voip_finalizados': voip_finalizados})


#  ------------------------------------------------------------------------
#  ------------------------------------------------------------------------
#  ------------------------------------------------------------------------


class SolicitarPortabilidadeVoip(CreateView):
    model = ServicoVoip
    form_class = SolicitarPortabilidadeVoipForm
    success_url = '/voip/'
    template_name = 'voip/solicitar-portabilidade-voip.html'

    def form_valid(self, form):
        form.instance.portabilidade_voip = 'True'
        form.instance.reservado_voip = 'True'
        return super(SolicitarPortabilidadeVoip, self).form_valid(form)


def ListaPortabilidadeAguardando(request):
    portabilidade_aguardando = ServicoVoip.objects.filter(reservado_voip='True').filter(portabilidade_voip='True').\
        filter(portabilidade_analise='False').filter(finalizado_voip='False').filter(boleto_entregue='False')
    conetext = {
        'portabilidade_aguardando': portabilidade_aguardando
    }
    return render(request, 'voip/lista-portabilidade-aguardando.html', conetext)


def ListaPortabilidadeAnalise(request):
    portabilidade_analise = ServicoVoip.objects.filter(reservado_voip='True').\
        filter(portabilidade_voip='True'). \
        filter(portabilidade_analise='True').\
        filter(finalizado_voip='False').\
        filter(boleto_entregue='False')
    context = {
        'portabilidade_analise': portabilidade_analise
    }
    return render(request, 'voip/lista-portabilidade-analise.html', context)


def PortabilidadeEnviarAnalise(request, id=None):
    numero_voip = get_object_or_404(ServicoVoip, id=id)
    form = PortabilidadeEnviarAnaliseForm(request.POST or None, instance=numero_voip)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.portabilidade_analise = 'True'
        obj = form.save()
        obj.save()
        messages.success(request, 'Portabilidade encaminhada para a análise!')
        return redirect('/voip/')
    return render(request, 'voip/portabilidade-enviar-analise.html', {'form': form})


def FinalizarPortabiliadeVoip(request, id=None):
    portabilidade_voip = get_object_or_404(ServicoVoip, id=id)
    form = FinalizarNumeroVoipForm(request.POST or None, instance=portabilidade_voip)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.finalizado_voip = 'True'
        obj = form.save()
        obj.save()
        messages.success(request, 'Número finalizado com sucesso!')
        return redirect('/voip/')
    context = {
        'form': form,
        'portabilidade_voip': portabilidade_voip
    }
    return render(request, 'voip/finalizar-portabilidade-voip.html', context)


def ListaPortabilidadeFinalizados(request):
    portabilidade_finalizados = ServicoVoip.objects.filter(reservado_voip='True'). \
        filter(portabilidade_voip='True'). \
        filter(portabilidade_analise='True'). \
        filter(finalizado_voip='True')
    context = {
        'portabilidade_finalizados': portabilidade_finalizados
    }
    return render(request, 'voip/lista-portabilidade-finalizados.html', context)


#  ------------------------------------------------------------------------
#  ------------------------------------------------------------------------
#  ------------------------------------------------------------------------


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
    return render(request, 'voip/finalizar-numero-voip.html', {'form': form, 'numero_voip': numero_voip})


def FinalizarNumeroVoipSemBoleto(request, id=None):
    numero_voip = get_object_or_404(ServicoVoip, id=id)
    form = FinalizarNumeroVoipSemBoletoForm(request.POST or None, instance=numero_voip)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.boleto_entregue = 'True'
        obj = form.save()
        obj.save()
        messages.success(request, 'Boleto verificado!')
        return redirect('/voip/')
    return render(request, 'voip/finalizar-numero-voip-sem-boleto.html', {'form': form})
