# Generated by Django 3.0 on 2021-05-21 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20210521_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamento',
            name='motivo_pagamento',
            field=models.CharField(max_length=255, verbose_name='Motivo do pagamento'),
        ),
    ]