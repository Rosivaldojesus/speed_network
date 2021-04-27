from django.contrib import admin
from .models import Instalacao


# Register your models here.
class InstalacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cliente', 'data_criacao')


admin.site.register(Instalacao, InstalacaoAdmin)
