from django.contrib import admin
from .models import Manuais

# Register your models here.

class ManuaisAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_manual','texto_manual')
admin.site.register(Manuais, ManuaisAdmin)