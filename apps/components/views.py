from django.shortcuts import render
from .models import Instalacao

# Create your views here.
from django.views.generic import CreateView


def Index(request):
    return render(request, 'components/instalacao.html')

def CadastroInstalacao(request):
    nome_cliente = request.POST.get('nome_cliente')
    cpf_cliente = request.POST.get('cpf_cliente')
    rg_cliente = request.POST.get('rg_cliente')
    rua_cliente = request.POST.get('rua_cliente')
    bairro_cliente = request.POST.get('bairro_cliente')
    numero_endereco_cliente = request.POST.get('numero_endereco_cliente')
    cidade_cliente = request.POST.get('cidade_cliente')
    uf_cliente = request.POST.get('uf_cliente')
    telefone_cliente = request.POST.get('telefone_cliente')
    email_cliente = request.POST.get('email_cliente')


    return render(request, 'components/cadastro-instalacao.html')