# Generated by Django 3.0 on 2021-05-13 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0011_instalacao_boleto_entregue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instalacao',
            name='data_concluido',
            field=models.DateTimeField(),
        ),
    ]
