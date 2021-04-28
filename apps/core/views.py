from django.db.models import Q
from django.shortcuts import render
from ..sales.models import Instalacao
from ..core.models import Manuais

# Create your views here.
def Index(request):
    pendentes = Instalacao.objects.all().count()
    instalando = Instalacao.objects.filter(instalando=True).count()

    return render(request, 'core/index.html',{'pendentes':pendentes,
                                              'instalando':instalando,
                                              })

def ManuaisServicos(request):
    manuais = Manuais.objects.all()
    queryset = request.GET.get('q')
    if queryset:
        manuais = Manuais.objects.filter(
            Q(nome_manual__icontaians=queryset)
        )
    return render(request, 'core/manuais.html', {'manuais':manuais})