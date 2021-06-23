from django.db.models import F, Q
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CtoForm, CadastroCtoForm
from .models import TerminaisOpticos


# Create your views here
def Index(request):
    ctos = TerminaisOpticos.objects.annotate(livre=F('conexoes_opticas_cto') - F('quant_conexoes_usadas_cto'))\
        .order_by('rua_cto')
    queryset = request.GET.get('q')
    if queryset:
        ctos = TerminaisOpticos.objects.annotate(livre=F('conexoes_opticas_cto') - F('quant_conexoes_usadas_cto'))\
            .order_by('rua_cto').filter(Q(rua_cto__icontains=queryset))
    quant_cto_cadastradas = TerminaisOpticos.objects.all().count()
    quant_cto_completas = TerminaisOpticos.objects.filter(conexoes_opticas_cto=F("quant_conexoes_usadas_cto")) \
        .annotate(livre=F('conexoes_opticas_cto') - F('quant_conexoes_usadas_cto')).count()
    return render(request, 'cto/terminais-opticos.html',{'ctos': ctos,
                                                         'quant_cto_completas': quant_cto_completas,
                                                         'quant_cto_cadastradas': quant_cto_cadastradas})


@login_required(login_url='/login/')
def InserirCto(request):
    form = CadastroCtoForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, 'A Cto foi inserida com sucesso!')
    else:
        form = CadastroCtoForm()
    return render(request, 'cto/inserir-cto.html', {'form': form})


@login_required(login_url='/login/')
def CadastrarCto(request):
    form = CtoForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'CTO cadastrada com sucesso.')
    else:
        form = CtoForm()
    return render(request, 'cto/cadastro-cto.html', {'form': form})


@login_required(login_url='/login/')
def EditarCto(request, id=None):
    cto = get_object_or_404(TerminaisOpticos, id=id)
    form = CtoForm(request.POST or None, instance=cto)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Boleto finalizado com sucesso.')
        return redirect('/cto/')
    return render(request, 'cto/editar-terminais-opticos.html', {'form': form})


def CtoCompletas(request):
    cto_completas = TerminaisOpticos.objects.filter(conexoes_opticas_cto=F("quant_conexoes_usadas_cto"))\
        .annotate(livre=F('conexoes_opticas_cto') - F('quant_conexoes_usadas_cto'))
    queryset = request.GET.get('q')
    if queryset:
        cto_completas = TerminaisOpticos.objects.filter(conexoes_opticas_cto=F("quant_conexoes_usadas_cto")) \
            .annotate(livre=F('conexoes_opticas_cto') - F('quant_conexoes_usadas_cto')).filter(
            Q(rua_cto__icontains=queryset))
    return render(request, 'cto/cto-completas.html', {'cto_completas': cto_completas})