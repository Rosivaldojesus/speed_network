# Generated by Django 3.0 on 2021-12-13 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0010_bairros'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datavencimento',
            options={'verbose_name_plural': 'Datas Vencimento'},
        ),
        migrations.AlterField(
            model_name='datavencimento',
            name='data',
            field=models.CharField(max_length=100, verbose_name='Data de Vencimento'),
        ),
    ]
