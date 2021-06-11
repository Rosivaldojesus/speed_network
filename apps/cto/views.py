from django.shortcuts import render, redirect
from django.db.models import F
from django.urls import reverse, reverse_lazy
from django.db.models import Q, Count
from .forms import CtoForm
from django.contrib import messages
from .models import TerminaisOpticos
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here
def Index(request):
    ctos = TerminaisOpticos.objects.annotate(livre=F('conexoes_opticas_cto') - F('quant_conexoes_usadas_cto')).order_by('rua_cto')
    queryset = request.GET.get('q')
    if queryset:
        ctos = TerminaisOpticos.objects.filter(
            Q(rua_cto__icontains=queryset))
    return render(request, 'cto/terminais-opticos.html',{'ctos': ctos})



def CadastroCto(request):
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







