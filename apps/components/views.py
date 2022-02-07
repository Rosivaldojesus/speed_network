from django.shortcuts import render
from django.db.models import Q
from .models import Ruas
import csv
from django.http import HttpResponse


# Create your views here.
def Index(request):
    return render(request, 'components/indexxx.html')


def DirecionamentoServicos(request):
    return render(request, 'components/direcionamento-servicos.html')


def RuasAtendidas(request):
    ruas = Ruas.objects.all()
    quant_ruas = Ruas.objects.all().count()
    queryset = request.GET.get('q')
    if queryset:
        ruas = Ruas.objects.filter(
            Q(logradouro__icontains=queryset) |
            Q(bairro__icontains=queryset) |
            Q(cep__icontains=queryset) |
            Q(logradouro__icontains=queryset))
        quant_ruas = Ruas.objects.filter(
            Q(logradouro__icontains=queryset) |
            Q(bairro__icontains=queryset) |
            Q(cep__icontains=queryset) |
            Q(logradouro__icontains=queryset)).count()
    context = {
        'ruas': ruas,
        'quant_ruas': quant_ruas
    }
    return render(request, 'components/ruas.html', context)


#  Exportando os dados para CSV
def ExportarRuasCSV(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="listagem-ruas.csv"'

    ruas = Ruas.objects.all()

    writer = csv.writer(response)
    writer.writerow(
        [
            'id', 'logradouro', 'bairro', 'cep', 'numero_baixo', 'numero_alto',
        ]
    )
    for rua in ruas:
        writer.writerow([rua.id, rua.logradouro, rua.bairro, rua.cep, rua.numero_baixo, rua.numero_alto])
    return response
