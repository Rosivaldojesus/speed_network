from django.shortcuts import render
from ..sales.models import Instalacao

# Create your views here.
def Index(request):
    pendentes = Instalacao.objects.all().count()
    instalando = Instalacao.objects.filter(instalando=True).count()

    return render(request, 'core/index.html',{'pendentes':pendentes,
                                              'instalando':instalando,
                                              })