from django.shortcuts import render
from .models import Instalacao
from ..components.models import PlanosInternet
from .forms import InstalacaoForm

# Create your views here.
def Index(request):
    return render(request, 'sales/instalacao.html')

def CadastroInstalacao(request):
    form = InstalacaoForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
    else:
        form = InstalacaoForm()

    return render(request, 'sales/cadastro-instalacao.html', {'form': form})