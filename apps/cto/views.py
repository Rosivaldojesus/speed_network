from django.db.models import F, Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import CtoForm, CaixasDeEmendaForm, InsertCtoForm
from .models import TerminaisOpticos, Primarias, CaixasDasPrimarias
from .models import CaixasDeEmenda, PonPorCaixaEmenda
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect, get_object_or_404
import csv


# Create your views here


@login_required(login_url='/login/')
def Index(request):
    ctos = TerminaisOpticos.objects.annotate(livre=F('conexoes_opticas_cto') - F('quant_conexoes_usadas_cto'))\
        .order_by('rua_cto').order_by('bairro_cto')
    # Verifica a quantidade de Ctos Filtradas
    quant_cto_filtradas = TerminaisOpticos.objects.all().count()
    quant_cto_cadastradas = TerminaisOpticos.objects.all().count()
    quant_caixas_emenda = CaixasDeEmenda.objects.all().count()
    quant_caixas_primarias = Primarias.objects.all().count()

    board = request.GET.get('board')
    pon = request.GET.get('pon')
    queryset = request.GET.get('q')

    if board and pon:
        ctos = TerminaisOpticos.objects.annotate(
            livre=F('conexoes_opticas_cto') - F('quant_conexoes_usadas_cto')).order_by('rua_cto')\
            .filter(board_cto__exact=board, pon_cto__exact=pon).order_by('codigo_cto')
        quant_cto_filtradas = TerminaisOpticos.objects.annotate(
            livre=F('conexoes_opticas_cto') - F('quant_conexoes_usadas_cto'))\
            .order_by('rua_cto').filter(board_cto__exact=board, pon_cto__exact=pon).count()
    elif queryset:
        ctos = TerminaisOpticos.objects.annotate(livre=F(
            'conexoes_opticas_cto') - F('quant_conexoes_usadas_cto')).order_by('rua_cto')\
            .filter(Q(rua_cto__icontains=queryset) | Q(codigo_cto__icontains=queryset))
        quant_cto_filtradas = TerminaisOpticos.objects.annotate(
            livre=F('conexoes_opticas_cto') - F('quant_conexoes_usadas_cto')).order_by('rua_cto')\
            .filter(Q(rua_cto__icontains=queryset) | Q(codigo_cto__icontains=queryset)).count()

    quant_cto_completas = TerminaisOpticos.objects.filter(conexoes_opticas_cto=F("quant_conexoes_usadas_cto")) \
        .annotate(livre=F('conexoes_opticas_cto') - F('quant_conexoes_usadas_cto')).count()

    boards = TerminaisOpticos.objects.all()
    pons = TerminaisOpticos.objects.all()

#Contagem de CTO´s por bairros

    quant_cto_ayrosa = TerminaisOpticos.objects.filter(bairro_cto=1).count()
    quant_cto_vl_remedios = TerminaisOpticos.objects.filter(bairro_cto=2).count()
    quant_cto_jd_belaura = TerminaisOpticos.objects.filter(bairro_cto=3).count()
    quant_cto_jd_mutinga = TerminaisOpticos.objects.filter(bairro_cto=4).count()
    quant_cto_jaguara = TerminaisOpticos.objects.filter(bairro_cto=5).count()
    quant_cto_jd_rochhale = TerminaisOpticos.objects.filter(bairro_cto=6).count()
    quant_cto_jd_marisa = TerminaisOpticos.objects.filter(bairro_cto=7).count()

    context = {
        'ctos': ctos,
        'quant_cto_completas': quant_cto_completas,
        'quant_cto_cadastradas': quant_cto_cadastradas,
        'boards': boards,
        'pons': pons,
        'quant_cto_filtradas': quant_cto_filtradas,
        'quant_caixas_emenda': quant_caixas_emenda,
        'quant_caixas_primarias': quant_caixas_primarias,
        'quant_cto_ayrosa': quant_cto_ayrosa,
        'quant_cto_vl_remedios': quant_cto_vl_remedios,
        'quant_cto_jd_belaura': quant_cto_jd_belaura,
        'quant_cto_jd_mutinga': quant_cto_jd_mutinga,
        'quant_cto_jaguara': quant_cto_jaguara,
        'quant_cto_jd_rochhale': quant_cto_jd_rochhale,
        'quant_cto_jd_marisa': quant_cto_jd_marisa,
    }
    return render(request, 'cto/index.html', context)


@login_required(login_url='/login/')
def EditarCto(request, id=None):
    cto = get_object_or_404(TerminaisOpticos, id=id)
    form = CtoForm(request.POST or None, instance=cto)
    if form.is_valid():
        obj = form.save()
        obj.save()
        return redirect('/cto/')
    return render(request, 'cto/cto_formulario.html', {'form': form})


def CtoCompletas(request):
    cto_completas = TerminaisOpticos.objects.filter(conexoes_opticas_cto=F("quant_conexoes_usadas_cto"))\
        .annotate(livre=F('conexoes_opticas_cto') - F('quant_conexoes_usadas_cto'))
    queryset = request.GET.get('q')
    if queryset:
        cto_completas = TerminaisOpticos.objects.filter(conexoes_opticas_cto=F("quant_conexoes_usadas_cto")) \
            .annotate(livre=F('conexoes_opticas_cto') - F('quant_conexoes_usadas_cto')).filter(
            Q(rua_cto__icontains=queryset))

    context = {
        'cto_completas': cto_completas
    }
    return render(request, 'cto/cto-completas.html', context)


class CTOCreate(CreateView):
    model = TerminaisOpticos
    template_name = "cto/cto_formulario.html"
    form_class = InsertCtoForm
    success_url = '/cto/'
    success_message = "%(nome_cliente)s, foi cadastrado com sucesso!!!"


def ExportarCSVCTO(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="lista_de_cto.csv"'
    ctos = TerminaisOpticos.objects.all()
    writer = csv.writer(response)
    writer.writerow(
        [
            'id', 'codigo_cto', 'rua_cto', 'numero_rua_cto', 'bairro', 'pon_cto', 'conexoes_opticas_cto',
            'board_cto', 'quant_conexoes_usadas_cto'
        ]
    )
    for cto in ctos:
        writer.writerow(
            [
                cto.id, cto.codigo_cto, cto.rua_cto, cto.numero_rua_cto, cto.bairro, cto.pon_cto,
                cto.conexoes_opticas_cto, cto.board_cto, cto.quant_conexoes_usadas_cto
            ]
        )
    return response


# ------------------------- Caixas de Emenda ----------------


def CaixasEmenda(request):
    caixa_emenda = CaixasDeEmenda.objects.all().order_by('-id')
    context = {
        'caixa_emenda': caixa_emenda
    }
    return render(request, 'cto/caixas-emenda.html', context)


@login_required(login_url='/login/')
def CaixaEmendaVisualizacao(request):
    caixa = request.GET.get('id')
    if caixa:
        caixa = CaixasDeEmenda.objects.get(id=caixa)
        pons = PonPorCaixaEmenda.objects.filter(caixa_emenda=caixa)

    context = {
        'caixa': caixa,
        'pons': pons
    }
    return render(request, 'cto/visualizar-caixa_emenda.html', context)


def ExportarCSVCaixasEmenda(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="caixas-emenda.csv"'

    caixas_emenda = CaixasDeEmenda.objects.all()

    writer = csv.writer(response)
    writer.writerow(['id', 'codigo_caixa', 'rua_caixa_emenda', 'numero_rua_cto'])
    for caixa in caixas_emenda:
        writer.writerow([caixa.id, caixa.codigo_caixa, caixa.rua_caixa_emenda, caixa.numero_rua_cto])
    return response


"""
#---------------------- Caixas de Emenda ---------------------------------------
--------------------------------------------------------------------------------
"""


class CaixasEmendaCreate(CreateView):
    model = CaixasDeEmenda
    fields = ['codigo_caixa', 'rua_caixa_emenda', 'numero_rua_cto']
    success_url = '/cto/caixas-emenda/'


@login_required(login_url='/login/')
def CadastrarCaixaEmenda(request):
    form = CaixasDeEmendaForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, 'Caixa de emenda criada  com sucesso!')
    else:
        form = CaixasDeEmendaForm()
    return render(request, 'cto/caixasdeemenda_form.html', {'form': form})


@login_required(login_url='/login/')
def EditarCaixasEmendas(request, id=None):
    caixa = get_object_or_404(CaixasDeEmenda, id=id)
    form = CaixasDeEmendaForm(request.POST or None, instance=caixa)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Caixa atualizada com sucesso')
        return redirect('/cto/')
    return render(request, 'cto/editar-caixas-emenda.html', {'form': form})


"""
-------------------------- Primárias ---------------------------------------
"""


def Primaria(request):
    primarias = Primarias.objects.all()
    queryset = request.GET.get('q')
    if queryset:
        primarias = Primarias.objects.filter(Q(pon__icontains=queryset))
    return render(request, 'cto/primarias.html', {'primarias': primarias})


class PrimariasCreate(CreateView):
    model = Primarias
    fields = ['board', 'pon', 'localizacao', 'quant_caixas']
    success_url = '/cto/primarias/'


def VisualizarCaixasPrimarias(request):
    caixas = request.GET.get('id')
    if caixas:
        caixas = CaixasDasPrimarias.objects.filter(primaria=caixas)

    context = {
        'caixas': caixas

    }
    return render(request, 'cto/caixas-primarias.html', context)
