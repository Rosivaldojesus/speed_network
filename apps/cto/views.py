from django.db.models import F, Q
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CtoForm, InsertCtoForm, CaixasDeEmendaForm
from .models import TerminaisOpticos
from .models import CaixasDeEmenda, PonPorCaixaEmenda
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView


# Create your views here
def Index(request):
    ctos = TerminaisOpticos.objects.annotate(livre=F('conexoes_opticas_cto') - F('quant_conexoes_usadas_cto'))\
        .order_by('rua_cto')
    queryset = request.GET.get('q')
    if queryset:
        ctos = TerminaisOpticos.objects.annotate(livre=F('conexoes_opticas_cto') - F('quant_conexoes_usadas_cto'))\
            .order_by('rua_cto').filter(Q(rua_cto__icontains=queryset)|
                                        Q(codigo_cto__icontains=queryset))
    quant_cto_cadastradas = TerminaisOpticos.objects.all().count()
    quant_cto_completas = TerminaisOpticos.objects.filter(conexoes_opticas_cto=F("quant_conexoes_usadas_cto")) \
        .annotate(livre=F('conexoes_opticas_cto') - F('quant_conexoes_usadas_cto')).count()
    return render(request, 'cto/terminais-opticos.html',{'ctos': ctos,
                                                         'quant_cto_completas': quant_cto_completas,
                                                         'quant_cto_cadastradas': quant_cto_cadastradas,
                                                         })

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

def InsertCto(request):
    form = InsertCtoForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, 'CTO Inserida')
    else:
        form = InsertCtoForm()
    return render(request, 'cto/add-cto.html', {'form':form})

# ------------------------- Caixas de Emenda ----------------
def CaixasEmenda(request):
    caixa_emenda = CaixasDeEmenda.objects.all().order_by('-id')
    return render(request, 'cto/caixas-emenda.html', {'caixa_emenda': caixa_emenda} )



@login_required(login_url='/login/')
def CaixaEmendaVisualizacao(request):
    caixa = request.GET.get('id')
    if caixa:
        caixa = CaixasDeEmenda.objects.get(id=caixa)
        pons = PonPorCaixaEmenda.objects.filter(caixa_emenda=caixa)
    return render(request, 'cto/visualizar-caixa_emenda.html',{'caixa': caixa,
                                                               'pons':pons})

#---------------------- Caixas de Emenda ---------------------------------------
class CaixaEmendaCreate(CreateView):
    model = CaixasDeEmenda
    fields = ['codigo_caixa',
              'rua_caixa_emenda',
              'numero_rua_cto',
             ]
    success_url = '/cto/'


@login_required(login_url='/login/')
def CadastrarCaixaEmenda (request):
    form = CaixasDeEmendaForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, 'Caixa de emenda criada  com sucesso!')
        #return redirect('/cto/caixas-emenda/')
    else:
        form = CaixasDeEmendaForm()
    return render(request, 'cto/cadastrar-caixas-emenda.html',{'form':form})


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
