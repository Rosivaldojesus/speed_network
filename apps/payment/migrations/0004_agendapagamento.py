# Generated by Django 3.0 on 2021-05-25 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20210521_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaPagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo_pagamento', models.CharField(max_length=255, verbose_name='Motivo do pagamento')),
                ('data_pagamento', models.DateField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='payment.CategoriaPagamento')),
            ],
            options={
                'verbose_name_plural': ' Agenda Pagamento',
            },
        ),
    ]
