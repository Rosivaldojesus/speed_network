from django.shortcuts import render
from .models import TerminaisOpticos

# Create your views here

def Index(request):
    ctos = TerminaisOpticos.objects.all()
    return render(request, 'cto/terminais-opticos.html',{'ctos': ctos})


