# Generated by Django 3.0 on 2021-08-23 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voip', '0002_servicovoip_portabilidade_analise'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicovoip',
            name='observacao_instalacao',
            field=models.TextField(blank=True, null=True, verbose_name='Observação'),
        ),
    ]
