from datetime import datetime, date, timedelta
from django.db.models.functions import TruncMonth
from django.db.models import Q,Count

from apps.sales.models import Instalacao

this_month = date.today().month
this_year = datetime.now().year
last_year = datetime.now().year -1
this_month = datetime.now().month
last_month = (datetime.today() - timedelta(days=30)).month


def quantidade_concluida():
    quant_concluida = Instalacao.objects.filter(concluido='True').count()
    return quant_concluida


def quantidade_instalacoes_mes_atual():
    total = Instalacao.objects.filter(
        data_finalizacao__month=this_month, data_finalizacao__year=this_year, concluido='True'
        ).count()
    return total


def quantidade_instalacoes_em_aberto():
    quant_aberta = Instalacao.objects.filter(status_agendada='False').filter(concluido='False').count()
    return quant_aberta


def quantidade_instalacoes_agendadas():
    quant_agendada = Instalacao.objects.filter(status_agendada='True').filter(concluido='False').count()
    return quant_agendada


def quantidade_instalacoes_sem_boleto():
    quant_sem_boleto = Instalacao.objects.filter(concluido='True').filter(boleto_entregue='False').count()
    return quant_sem_boleto


# --------------------------------------------------------------------------------------------------------------------
def quantidade_instalacoes_mensais():
    instalacoes_mensais = Instalacao.objects.annotate(month=TruncMonth('data_finalizacao')).filter(concluido='True').\
        values('month').annotate(c=Count('data_finalizacao')).values('month', 'c').order_by('month')
    return instalacoes_mensais


def quantidade_instalacoes_diarias():
    instalacoes_diarias = Instalacao.objects.filter(concluido='True').\
        filter(data_finalizacao__gte=datetime.today()-timedelta(days=30)).values('data_finalizacao').\
        annotate(number=Count('data_finalizacao')).order_by('data_finalizacao')
    return instalacoes_diarias

# --------------------------------------------------------------------------------------------------------------------
def quantidade_conheceu_empresa_count():
    resultado = Instalacao.objects.filter(como_conheceu_empresa__isnull=True).count()
    return resultado


def quantidade_conheceu_empresa_mes_count():
    resultado = Instalacao.objects.filter(data_finalizacao__month=this_month).count()
    return resultado


def quantidade_conheceu_por_panfletos():
    panfletos_count = Instalacao.objects.filter(Q(como_conheceu_empresa__icontains='Panfleto')).count()
    return panfletos_count

# ---->>> Filtrando instalação por Vendedor


def media_diario_instalacao():
    media_diario_instalacao = Instalacao.objects.annotate(month=TruncMonth('data_finalizacao')).\
        filter(concluido='True').values('month').annotate(c=Count('data_finalizacao')).values('month', 'c').\
        order_by('month')
    return media_diario_instalacao



 # ---->>> Filtros de como o cliente conheceu a empresa
def conheceu_redes_sociais_count():
    redes_sociais_count = Instalacao.objects.filter(Q(como_conheceu_empresa__icontains='Redes Socias')).count()
    return redes_sociais_count


def conheceu_site_count():
    site_count = Instalacao.objects.filter(Q(como_conheceu_empresa__icontains='Site')).count()
    return site_count


def conheceu_indicacao_count():
    indicacao_count = Instalacao.objects.filter(Q(como_conheceu_empresa__icontains='Indicação')).count()
    return indicacao_count


def conheceu_outros_count():
    outros_count = Instalacao.objects.filter(Q(como_conheceu_empresa__icontains='Outros')).count()
    return outros_count

# ---->>> Filtros de como o cliente conheceu a empresa mês atual

def conheceu_panfletos_mes_count():
    panfletos_mes_count = Instalacao.objects.filter(Q(como_conheceu_empresa__icontains='Panfleto')).\
        filter(data_finalizacao__month=this_month).count()
    return panfletos_mes_count


def conheceu_redes_sociais_mes_count():
    redes_sociais_mes_count = Instalacao.objects.filter(Q(como_conheceu_empresa__icontains='Redes Socias')).\
        filter(data_finalizacao__month=this_month).count()

    return redes_sociais_mes_count
def conheceu_site_mes_count():
    site_mes_count = Instalacao.objects.filter(Q(como_conheceu_empresa__icontains='Site')).\
        filter(data_finalizacao__month=this_month).count()
    return site_mes_count


def conheceu_indicacao_mes_count():
    indicacao_mes_count = Instalacao.objects.filter(Q(como_conheceu_empresa__icontains='Indicação')).\
        filter(data_finalizacao__month=this_month).count()
    return indicacao_mes_count

def conheceu_empresa_outros_mes_count():
    outros_mes_count = Instalacao.objects.filter(Q(como_conheceu_empresa__icontains='Outros')).\
        filter(data_finalizacao__month=this_month).count()
    return outros_mes_count