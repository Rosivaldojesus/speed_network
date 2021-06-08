from django.shortcuts import render


# Create your views here.

def Index(request):
    return render(request, 'components/index.html')

def DirecionamentoServicos(request):
    return render(request, 'components/direcionamento-servicos.html')



