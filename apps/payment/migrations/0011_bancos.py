# Generated by Django 3.0 on 2021-11-06 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0010_fluxoentradassaidas_saldodia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bancos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_banco', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Banco',
            },
        ),
    ]
