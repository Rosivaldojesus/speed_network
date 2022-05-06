from datetime import datetime, date, timedelta

from ..models import Instalacao


this_month = date.today().month
this_year = datetime.now().year
last_year = datetime.now().year -1
this_month = datetime.now().month
last_month = (datetime.today() - timedelta(days=30)).month



def instalacoes_mes_atual():
    total = Instalacao.objects.filter(
        data_finalizacao__month=this_month, data_finalizacao__year=this_year, concluido='True').count()
    return total
