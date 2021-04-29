from django.shortcuts import render
from .models import Pagamento

# Create your views here.
def Index(request):
    pagamentos = Pagamento.objects.all()
    return render(request, 'payment/index.html', {'pagamentos':pagamentos})

def CadastrarPagamento(request):
    return render(request, 'payment/cadastrar-pagamento.html')

