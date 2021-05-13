from django.contrib import admin
from .models import TerminaisOpticos

# Register your models here.

class TerminaisOpticosAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo_cto', 'pon_cto','conexoes_opticas_cto','quant_conexoes_usadas_cto')
admin.site.register(TerminaisOpticos, TerminaisOpticosAdmin)
