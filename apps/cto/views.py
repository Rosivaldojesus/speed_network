from django.shortcuts import render, redirect
from django.db.models import F
from django.urls import reverse, reverse_lazy

from .forms import CtoForm
from django.contrib import messages

from .models import TerminaisOpticos

# Create your views here

def Index(request):
    #ctos = TerminaisOpticos.objects.all()
    #ctos = TerminaisOpticos.objects.annotate(livre=F('quant_conexoes_usadas_cto') - F('conexoes_opticas_cto'),)
    ctos = TerminaisOpticos.objects.annotate(livre=F('conexoes_opticas_cto') - F('quant_conexoes_usadas_cto'))

    caixa = request.GET.get('id')
    if caixa:
        caixa = TerminaisOpticos.objects.get(id=caixa)

    return render(request, 'cto/terminais-opticos.html',{'ctos': ctos,
                                                         'caixa':caixa,})



def CadastroCto(request):
    form = CtoForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'CTO cadastrada com sucesso.')
    else:
        form = CtoForm()
    return render(request, 'cto/cadastro-cto.html', {'form': form})


