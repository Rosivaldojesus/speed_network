from django.shortcuts import render
from .models import Produto

# Create your views here.
def Index(request):
    produtos = Produto.objects.all()
    return render(request, 'stock/index.html', {'produtos': produtos})