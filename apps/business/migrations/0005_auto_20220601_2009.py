# Generated by Django 3.0 on 2022-06-01 23:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business', '0004_auto_20220601_1925'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='vendas_produtos',
            new_name='VendasProdutos',
        ),
    ]