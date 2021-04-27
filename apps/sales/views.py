from django.shortcuts import render
from .models import Instalacao
from ..components.models import PlanosInternet
from .forms import InstalacaoForm

# Create your views here.
def Index(request):
    instalacoes = Instalacao.objects.all()
    return render(request, 'sales/instalacao.html', {'instalacoes': instalacoes})

def CadastroInstalacao(request):
    form = InstalacaoForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
    else:
        form = InstalacaoForm()

    return render(request, 'sales/cadastro-instalacao.html', {'form': form})

def InstalacaoVisualizacao(request):
    install = request.GET.get('id')
    if install:
        install = Instalacao.objects.get(id=install)
    return render(request, 'sales/visualizar-instalacao.html',{'install': install})