# Generated by Django 3.0 on 2021-05-08 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0008_auto_20210508_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instalacao',
            name='data_instalacao',
            field=models.DateField(blank=True, null=True, verbose_name='Data da Instalação'),
        ),
    ]