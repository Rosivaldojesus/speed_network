from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView
from .models import PlanosInternet

from .models import Instalacao
from .forms import InstalacaoCreateForm, InstalacaoUpdateForm,\
    InstalacaoAgendarForm, InstalacaoFinalizarForm


# Create your views here.
def Index(request):
    instalacoes = Instalacao.objects.all().order_by('data_instalacao', 'data_instalacao')
    quant_aberta = Instalacao.objects.filter(status_agendada='False').filter(concluido='False').count()
    quant_agendada = Instalacao.objects.filter(status_agendada='True').filter(concluido='False').count()
    quant_concluida = Instalacao.objects.filter(concluido='True').count()
    return render(request, 'sales/instalacao.html', {'instalacoes': instalacoes,
                                                     'quant_aberta': quant_aberta,
                                                     'quant_agendada': quant_agendada,
                                                     'quant_concluida': quant_concluida,
                                                     })

def InstalacaoAberta(request):
    abertas = Instalacao.objects.filter(status_agendada='False').filter(concluido='False')
    return render(request, 'sales/instalacao-aberta.html', {'abertas': abertas,
                                                        })

def InstalacaoAgendada(request):
    agendadas = Instalacao.objects.filter(status_agendada='True')\
        .filter(concluido='False').order_by('data_instalacao', 'hora_instalacao')
    quant_agendada = Instalacao.objects.filter(status_agendada='True').count()
    return render(request, 'sales/instalacao-agendada.html', {'agendadas':agendadas,
                                                              'quant_agendada':quant_agendada})

def InstalacaoConcluida(request):
    concluidas = Instalacao.objects.filter(concluido='True')
    return render(request, 'sales/instalacao-concluida.html', {'concluidas': concluidas})
'''    
def Index(request):
    instalacoes = Instalacao.objects.all().order_by('data_instalacao', 'data_instalacao')
    return render(request, 'sales/instalacao.html', {'instalacoes': instalacoes})
'''

def CadastroInstalacao(request):
    form = InstalacaoCreateForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Instalação cadastrada com sucesso.')
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
        messages.success(request, 'Instalação editada com sucesso.')
        return redirect('/vendas/')
    return render(request, 'sales/editar-instalacao.html', {'form': form})



def InstalacaoAgendar(request, id=None):
    insta = get_object_or_404(Instalacao, id=id)
    form = InstalacaoAgendarForm(request.POST or None, instance=insta)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Instalação agendada com sucesso.')
        return redirect('/vendas/')
    return render(request, 'sales/agendar-instalacao.html', {'form': form})



def InstalacaoFinalizar(request, id=None):
    insta = get_object_or_404(Instalacao, id=id)
    form = InstalacaoFinalizarForm(request.POST or None, instance=insta)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Instalação finalizada com sucesso.')
        return redirect('/vendas/')
    return render(request, 'sales/finalizar-instalacao.html', {'form': form})



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




