from django.shortcuts import render
from django.db.models import F, Q
from .models import Ruas


# Create your views here.
def Index(request):
    return render(request, 'components/index.html')


def DirecionamentoServicos(request):
    return render(request, 'components/direcionamento-servicos.html')


def RuasAtendidas(request):
    ruas = Ruas.objects.all()
    queryset = request.GET.get('q')
    if queryset:
        ruas = Ruas.objects.filter(
            Q(logradouro__icontains=queryset)|
            Q(bairro__icontains=queryset)|
            Q(cep__icontains=queryset)|
            Q(logradouro__icontains=queryset))
    return render(request, 'components/ruas.html', {'ruas': ruas})



