from django.shortcuts import render, redirect, get_object_or_404
from .models import Instalacao
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
        return redirect('/vendas/')
    else:
        form = InstalacaoForm()
    return render(request, 'sales/cadastro-instalacao.html', {'form': form})


def InstalacaoVisualizacao(request):
    install = request.GET.get('id')
    if install:
        install = Instalacao.objects.get(id=install)
    return render(request, 'sales/visualizar-instalacao.html',{'install': install})



def InstalacaoEditar(request, id=None):
    insta = get_object_or_404(Instalacao, id=id)
    form = InstalacaoForm(request.POST or None, instance=insta)
    if form.is_valid():
        obj = form.save()
        obj.save()
        return redirect('/vendas/')
    return render(request, 'sales/editar-instalacao.html', {'form': form})




