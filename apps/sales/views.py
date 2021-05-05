from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView
from .models import PlanosInternet

from .models import Instalacao
from .forms import InstalacaoCreateForm, InstalacaoUpdateForm


# Create your views here.
def Index(request):
    instalacoes = Instalacao.objects.all().order_by('data_instalacao', 'data_instalacao')
    return render(request, 'sales/instalacao.html', {'instalacoes': instalacoes})


def CadastroInstalacao(request):
    form = InstalacaoCreateForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        return redirect('/vendas/')
    else:
        form = InstalacaoCreateForm()
    return render(request, 'sales/cadastro-instalacao.html', {'form': form})


    return render(request, 'sales/cadastro-instalacao.html', {'form':form})
'''
def CadastroInstalacao(request):
    form = InstalacaoCreateForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        return redirect('/vendas/')
    else:
        form = InstalacaoCreateForm()
    return render(request, 'sales/cadastro-instalacao.html', {'form': form})
'''

def InstalacaoVisualizacao(request):
    install = request.GET.get('id')
    if install:
        install = Instalacao.objects.get(id=install)
    return render(request, 'sales/visualizar-instalacao.html',{'install': install})



def InstalacaoEditar(request, id=None):
    insta = get_object_or_404(Instalacao, id=id)
    form = InstalacaoUpdateForm(request.POST or None, instance=insta)
    if form.is_valid():
        obj = form.save()
        obj.save()
        return redirect('/vendas/')
    return render(request, 'sales/editar-instalacao.html', {'form': form})



'''


def CadastroInstalacao(request):
    planos = Instalacao.objects.all()
    #messages.add_message(request, messages.SUCCESS, 'Usuário cadastrado com sucesso.')
    if request.method != 'POST':
        #messages.add_message(request, messages.WARNING, 'Nada cadastrado.')
        return render(request, 'sales/cadastro-instalacao.html', {'planos': planos})

    nome_cliente = request.POST.get('nome_cliente')
    data_instalacao = request.POST.get('data_instalacao')
    planos_instalacao = request.POST.get('planos_instalacao')

    install = Instalacao(nome_cliente=nome_cliente, data_instalacao=data_instalacao, planos_instalacao=planos_instalacao)
    install.save()
    return redirect('vendas')
    '''




