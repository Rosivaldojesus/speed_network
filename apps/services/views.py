import io
from datetime import datetime, date, timedelta
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ServicoForm, AgendarServicoForm, EditarAgendarServicoForm, FinalizarServicoForm
from .forms import ReservarVoipForm
from .models import Servico, ServicoVoip
from django.db.models import Q, Count
from django.views.generic.edit import CreateView
from django.db.models.functions import TruncMonth
# Create your views here.


def Index(request):
    this_month = date.today().month  # Variável do mês atual
    contarAbertos = Servico.objects.all().filter().filter(status_agendado='False').\
        filter(status_concluido='False').count()
    contarAgendados = Servico.objects.filter(status_agendado='True').\
        filter(status_concluido='False').filter(status_analise='False').count()

    contarFinalizados = Servico.objects.filter(data_finalizacao__month=this_month).filter(status_concluido='True').count()

    diarios = Servico.objects.all().filter(status_concluido='True').values('data_finalizacao').\
        annotate(number=Count('contato_servico'))
    servicosMensal = Servico.objects.annotate(month=TruncMonth('data_finalizacao')).filter(status_concluido='True').\
        values('month').annotate(c=Count('data_finalizacao')).values('month', 'c').order_by('month')
    diarioServicos = Servico.objects.filter(status_concluido='True').values('data_finalizacao').\
        filter(data_finalizacao__gte=datetime.today()-timedelta(days=30)).annotate(number=Count('data_finalizacao')).\
        order_by('data_finalizacao')

    #  Quantidade de serviços por categoria no mês atual

    quant_outros_mes = Servico.objects.filter(categoria=2).filter(data_finalizacao__month=this_month).count()
    quant_serv_velocidade_mes = Servico.objects.filter(categoria=3).filter(data_finalizacao__month=this_month).count()
    quant_serv_osciliacao_mes = Servico.objects.filter(categoria=4).filter(data_finalizacao__month=this_month).count()
    quant_serv_retirada_mes = Servico.objects.filter(categoria=5).filter(data_finalizacao__month=this_month).count()
    quant_serv_fibra_rompida_mes = Servico.objects.filter(categoria=6).\
        filter(data_finalizacao__month=this_month).count()
    quant_serv_troca_modem_mes = Servico.objects.filter(categoria=7).filter(data_finalizacao__month=this_month).count()
    quant_serv_voip_mes = Servico.objects.filter(categoria=8).filter(data_finalizacao__month=this_month).count()
    quant_serv_sinal_alto_mes = Servico.objects.filter(categoria=9).filter(data_finalizacao__month=this_month).count()
    quant_trocar_senha_mes = Servico.objects.filter(categoria=10).filter(data_finalizacao__month=this_month).count()

    #  Quantidade de serviços por categoria

    quant_outros = Servico.objects.filter(categoria=2).count()
    quant_serv_velocidade = Servico.objects.filter(categoria=3).count()
    quant_serv_osciliacao = Servico.objects.filter(categoria=4).count()
    quant_serv_retirada = Servico.objects.filter(categoria=5).count()
    quant_serv_fibra_rompida = Servico.objects.filter(categoria=6).count()
    quant_serv_troca_modem = Servico.objects.filter(categoria=7).count()
    quant_serv_voip = Servico.objects.filter(categoria=8).count()
    quant_serv_sinal_alto = Servico.objects.filter(categoria=9).count()
    quant_trocar_senha = Servico.objects.filter(categoria=10).count()

    #  Quantidade de serviços por categoria
    quant_serv_abertos_outros = Servico.objects.filter(categoria=2).filter(status_concluido='False').count()
    quant_serv_abertos_velocidade = Servico.objects.filter(categoria=3).filter(status_concluido='False').count()
    quant_serv_abertos_osciliacao = Servico.objects.filter(categoria=4).filter(status_concluido='False').count()
    quant_serv_abertos_retirada = Servico.objects.filter(categoria=5).filter(status_concluido='False').count()
    quant_serv_abertos_fibra_rompida = Servico.objects.filter(categoria=6).filter(status_concluido='False').count()
    quant_serv_abertos_troca_modem = Servico.objects.filter(categoria=7).filter(status_concluido='False').count()
    quant_serv_abertos_voip = Servico.objects.filter(categoria=8).filter(status_concluido='False').count()
    quant_serv_abertos_sinal_alto = Servico.objects.filter(categoria=9).filter(status_concluido='False').count()
    quant_serv_abertos_trocar_senha = Servico.objects.filter(categoria=10).filter(status_concluido='False').count()

    quant_retiradas_agendados = Servico.objects.filter(status_agendado='True').filter(status_concluido='False'). \
        filter(status_analise='True').count()

    context = {
        'contarAbertos': contarAbertos,
        'contarFinalizados': contarFinalizados,
        'contarAgendados': contarAgendados,
        'diarios': diarios,
        'servicosMensal': servicosMensal,
        'diarioServicos': diarioServicos,

        #  Quantidade de serviços por categorias mês atual
        'quant_serv_velocidade_mes': quant_serv_velocidade_mes,
        'quant_serv_osciliacao_mes': quant_serv_osciliacao_mes,
        'quant_serv_retirada_mes': quant_serv_retirada_mes,
        'quant_serv_fibra_rompida_mes': quant_serv_fibra_rompida_mes,
        'quant_serv_troca_modem_mes': quant_serv_troca_modem_mes,
        'quant_serv_voip_mes': quant_serv_voip_mes,
        'quant_serv_sinal_alto_mes': quant_serv_sinal_alto_mes,
        'quant_outros_mes': quant_outros_mes,
        'quant_trocar_senha_mes': quant_trocar_senha_mes,

        # Quantidade de serviços por categorias
        'quant_serv_abertos_outros': quant_serv_abertos_outros,
        'quant_serv_abertos_velocidade': quant_serv_abertos_velocidade,
        'quant_serv_abertos_osciliacao': quant_serv_abertos_osciliacao,
        'quant_serv_abertos_retirada': quant_serv_abertos_retirada,
        'quant_serv_abertos_fibra_rompida': quant_serv_abertos_fibra_rompida,
        'quant_serv_abertos_troca_modem': quant_serv_abertos_troca_modem,
        'quant_serv_abertos_voip': quant_serv_abertos_voip,
        'quant_serv_abertos_sinal_alto': quant_serv_abertos_sinal_alto,
        'quant_serv_abertos_trocar_senha': quant_serv_abertos_trocar_senha,

        # Quantidade de serviços por categorias
        'quant_serv_velocidade': quant_serv_velocidade,
        'quant_serv_osciliacao': quant_serv_osciliacao,
        'quant_serv_retirada': quant_serv_retirada,
        'quant_serv_fibra_rompida': quant_serv_fibra_rompida,
        'quant_serv_troca_modem': quant_serv_troca_modem,
        'quant_serv_voip': quant_serv_voip,
        'quant_serv_sinal_alto': quant_serv_sinal_alto,
        'quant_outros': quant_outros,
        'quant_trocar_senha': quant_trocar_senha,

        'quant_retiradas_agendados': quant_retiradas_agendados,


    }
    return render(request, 'services/index.html', context)


def CadastroServico(request):
    form = ServicoForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.criado_por = request.user
        obj = form.save()
        obj.save()
        messages.success(request, 'Serviço adicionado com sucesso!')
        return redirect('/servicos/')
    else:
        form = ServicoForm()
    return render(request, 'services/cadastro-servico.html', {'form': form})


def EditarServico(request, id=None):
    editar = get_object_or_404(Servico, id=id)
    form = ServicoForm(request.POST or None, instance=editar)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Serviço editado com sucesso!')
        return redirect('/servicos/servicos-abertos/')
    return render(request, 'services/editar-servico.html', {'form': form})


def RemoverServico(request, id=None):
    servico = get_object_or_404(Servico, id=id)
    if request.method == "POST":
        servico.delete()
        messages.success(request, 'Serviço removido com sucesso!')
        return redirect('/servicos/')
    context = {
        'servoco': servico
    }
    return render(request, 'services/deletar-servico.html', context)


def ServicosAbertos(request):
    abertos = Servico.objects.order_by('-id')\
        .filter(status_agendado='False')\
        .filter(status_concluido='False')
    qquant_aberto = Servico.objects.filter(status_agendado='False').filter(status_concluido='False').count()
    context = {
        'abertos': abertos,
        'qquant_aberto': qquant_aberto
    }
    return render(request, 'services/servicos-abertos.html', context)


def EditarServicoAgendado(request, id=None):
    editarAgendado = get_object_or_404(Servico, id=id)
    form = EditarAgendarServicoForm(request.POST or None, instance=editarAgendado)
    if form.is_valid():
        obj = form.save()
        obj.save()
        messages.success(request, 'Serviço agendado, editado com sucesso!')
        return redirect('/servicos/')
    return render(request, 'services/editar-servico.html', {'form': form})


def ServicosAgendados(request):
    agendados = Servico.objects.filter(status_agendado='True').filter(status_concluido='False').filter(status_analise='False').\
        order_by('data_agendada', 'hora_agendada')
    quant_agendados = Servico.objects.filter(status_agendado='True').filter(status_concluido='False').filter(status_analise='False').count()

    queryset = request.GET.get('q')
    startdate = request.GET.get('date')

    if queryset:
        agendados = Servico.objects.filter(Q(contato_servico__icontains=queryset)).filter(status_concluido='False')
        quant_agendados = Servico.objects.filter(Q(contato_servico__icontains=queryset)).\
            filter(status_concluido='False').filter(status_analise='False').count()

    if startdate:
        agendados = Servico.objects.filter(Q(data_agendada__exact=startdate)).filter(status_concluido='False').filter(status_analise='False')
        quant_agendados = Servico.objects.filter(Q(data_agendada__icontains=startdate)).\
            filter(status_concluido='False').filter(status_analise='False').count()

    quant_retiradas_agendados = Servico.objects.filter(status_agendado='True').filter(status_concluido='False'). \
        filter(status_analise='True').count()

    context = {
        'agendados': agendados,
        'quant_agendados': quant_agendados,
        'quant_retiradas_agendados': quant_retiradas_agendados,
    }
    return render(request, 'services/servicos-agendados.html', context)


def servicos_retiradas_agendados(request):
    agendados = Servico.objects.filter(status_agendado='True').filter(status_concluido='False').\
        filter(status_analise='True').order_by('data_agendada', 'hora_agendada')
    quant_agendados = Servico.objects.filter(status_agendado='True').filter(status_concluido='False').\
    filter(status_analise='True').count()

    queryset = request.GET.get('q')
    startdate = request.GET.get('date')

    if queryset:
        agendados = Servico.objects.filter(Q(contato_servico__icontains=queryset)).filter(status_concluido='False').\
            filter(status_analise='True')
        quant_agendados = Servico.objects.filter(Q(contato_servico__icontains=queryset)).\
            filter(status_concluido='False').filter(status_analise='True').count()

    if startdate:
        agendados = Servico.objects.filter(Q(data_agendada__exact=startdate)).filter(status_concluido='False').\
            filter(status_analise='True')
        quant_agendados = Servico.objects.filter(Q(data_agendada__icontains=startdate)).\
            filter(status_concluido='False').filter(status_analise='True').count()

    context = {
        'agendados': agendados,
        'quant_agendados': quant_agendados
    }
    return render(request, 'services/servicos-de-retiradas-agendados.html', context)







def ServicosFinalizados(request):
    finalizados = Servico.objects.filter(status_concluido='True').order_by('-id')
    queryset = request.GET.get('q')
    if queryset:
        finalizados = Servico.objects.filter(
            Q(contato_servico__icontains=queryset))
    quant_finalizados = Servico.objects.filter(status_concluido='True').count()
    conetxt = {
        'finalizados': finalizados,
        'quant_finalizados': quant_finalizados
    }
    return render(request, 'services/servicos-finalizados.html', conetxt)


def AgendarServico(request, id=None):
    agendar = get_object_or_404(Servico, id=id)
    form = AgendarServicoForm(request.POST or None, instance=agendar)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.agendado_por = request.user
        obj = form.save()
        obj.save()
        messages.success(request, 'Serviço agendado com sucesso!')
        return redirect('/servicos/')
    return render(request, 'services/agendar-servico.html', {'form': form})


def FinalizarServico(request, id=None):
    finalizar = get_object_or_404(Servico, id=id)
    form = FinalizarServicoForm(request.POST or None, instance=finalizar)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.finalizado_por = request.user
        obj = form.save()
        obj.save()
        messages.success(request, 'Serviço finalizado com sucesso!')
        return redirect('/servicos/')
    return render(request, 'services/finalizar-servico.html', {'form': form})


def ServicoVisualizar(request):
    servico = request.GET.get('id')
    if servico:
        servico = Servico.objects.get(id=servico)
    context = {
        'servico': servico
    }
    return render(request, 'services/visualizar-servico.html', context)


def DeletarServico(request, id=None):
    servico = get_object_or_404(Servico, id=id)
    if request.method == "POST":
        servico.delete()
        return redirect('/servicos/')
    context = {
        'servico': servico
    }
    return render(request, 'services/deletar-servico.html', context)


#  -------------------------------- SERVIÇOS DE VOIP ------------------------------------------------------------------


def ServicosVoip(request):
    voipDisponivel = ServicoVoip.objects.all().filter(reservado_voip='False').filter(finalizado_voip='False')
    quantDisponivel = ServicoVoip.objects.all().filter(reservado_voip='False').filter(finalizado_voip='False').count()
    voipReservado = ServicoVoip.objects.all().filter(portabilidade_voip='False').filter(reservado_voip='True').\
        filter(finalizado_voip='False')
    voipReservadoPortabilidade = ServicoVoip.objects.all().filter(portabilidade_voip='True').\
        filter(reservado_voip='True').filter(finalizado_voip='False')
    context = {
        'voipDisponivel': voipDisponivel,
        'quantDisponivel': quantDisponivel,
        'voipReservado': voipReservado,
        'voipReservadoPortabilidade': voipReservadoPortabilidade
    }
    return render(request, 'services/servicos-voip.html', context)

def ServicosVoipDisponiveis(request):
    voipDisponivel = ServicoVoip.objects.all().filter(finalizado_voip='False')
    return render(request, 'services/servicos-voip-disponiveis.html', {'voipDisponivel': voipDisponivel})

def ServicosVoipReservados(request):
    voipReservados = ServicoVoip.objects.all().filter(finalizado_voip='False').filter(reservado_voip='True')
    quant_Reservados = ServicoVoip.objects.all().filter(finalizado_voip='False').filter(reservado_voip='True').count()
    context = {
        'voipReservados': voipReservados,
        'quant_Reservados': quant_Reservados
    }
    return render(request, 'services/servicos-voip-reservados.html', context)


def ReservarVoip(request, id=None):
    voip = get_object_or_404(ServicoVoip, id=id)
    form = ReservarVoipForm(request.POST or None, instance=voip)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.funcionario_reserva_voip = request.user
        obj.data_reserva_voip = date.today()
        obj = form.save()
        obj.save()
        messages.success(request, 'Voip reservado com sucesso!')
        return redirect('/servicos/servicos-voip/')
    return render(request, 'services/reservar-voip.html', {'form': form})


class ReservarVoipPortabilidadeCreate(CreateView):
    model = ServicoVoip
    fields = ['nome_usuario_voip', 'cpf_usuario_voip']
    success_url = '/servicos/'


#  =============== PDF ======================
from reportlab.pdfgen import canvas
from django.http import HttpResponse

def servicos_de_retiradas(request):
    # Crie o objeto HttpResponse com o cabeçalho de PDF apropriado.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=retiradas.pdf'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    # Crie o objeto PDF, usando o objeto response como seu "arquivo".
    # p = canvas.Canvas(response)

    # Desenhe coisas no PDF. Aqui é onde a geração do PDF acontece.
    # Veja a documentação do ReportLab para a lista completa de
    # funcionalidades.
    p.drawString(10, 100, "Hello world.")

    retiradas = Servico.objects.all()

    y = 750
    for retirada in retiradas:
        p.drawString(10, y, retirada)
        y -= 20

    # Feche o objeto PDF, e está feito.
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response




def relatorio_servicos_retiradas(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    # p.drawString(200, 810, 'Relatorio de Serviços')


    servicos = Servico.objects.filter()

    # p.drawString(0, 800, '_' * 150)
    y = 750

    quant_de_clientes = 0
    quant_de_sevicos = len(servicos)
    lista = [3, 6, 9, 12]


    for servico in servicos:
        # p.drawString(40, y, 'Cliente: %s' % ( servico.contato_servico))
        # y -= 20
        # p.drawString(40, y, 'Serviço: %s' % (servico.servico_para_executar))
        # y -= 20
        # p.drawString(40, y, 'Endereço: %s' % (servico.endereco_servico))
        # y -= 20
        # p.drawString(40, y, 'Observação: %s' % (servico.observacao))
        # y -= 20
        #
        # p.drawString(0, y, '_' * 120)
        # y -= 20



        if quant_de_clientes in lista:
            p.showPage()

            p.drawString(40, 780, 'Cliente: %s' % ( servico.contato_servico))
            p.drawString(40, 760, 'Serviço: %s' % (servico.servico_para_executar))
            p.drawString(40, 740, 'Endereço: %s' % (servico.endereco_servico))
            p.drawString(40, 720, 'Observação: %s' % (servico.observacao))
            # y -= 20
            # p.drawString(40, y, 'Endereço: %s' % (servico.endereco_servico))
            # y -= 20
            # p.drawString(40, y, 'Observação: %s' % (servico.observacao))
            # y -= 20

            # p.drawString(0, y, '_' * 120)
            # y -= 20

        quant_de_clientes = quant_de_clientes + 1


    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response