from django.test import TestCase
from apps.core.models import Manuais, SenhasEquipamentos
from apps.components.models import FabricanteEquipamentos

# Create your tests here.

class CoreModelTest(TestCase):
    def test_insert_into_manuais(self):
        manuais = Manuais.objects.create(
            nome_manual='Modem',
            texto_manual='Olá, mundo. Estou inserendo um texto'
        )
        manuais.full_clean()
        manuais.save()
        return manuais

    def test_insert_into_fabricantes_equipamentos(self):
        fabricante = FabricanteEquipamentos.objects.create(nome_fabricante='fabricante')
        fabricante.save()

        senhas = SenhasEquipamentos.objects.create(
            equipamento='Equipamento',
            ip_equipamento='192.168.1.1',
            login='login',
            senha='senha',
            fabricante=fabricante
        )
        senhas.save()
