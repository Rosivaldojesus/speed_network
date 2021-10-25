# Generated by Django 3.0 on 2021-10-23 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sales', '0028_auto_20210819_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancelamentos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome Cliente')),
                ('cpf', models.CharField(max_length=30, verbose_name='CPF do Cliente')),
                ('Endereco', models.CharField(max_length=255, verbose_name='Endereço do Cliente')),
                ('plano_internet', models.CharField(choices=[('69,90', '69,90'), ('89,90', '89,90'), ('99,90', '99,90'), ('119,90', '119,90'), ('149,90', '149,90')], max_length=6, verbose_name='Plano contratado')),
                ('data', models.DateField(blank=True, null=True, verbose_name='Data do serviço')),
                ('data_criacao', models.DateTimeField(auto_now=True)),
                ('atendente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Atendente')),
            ],
            options={
                'verbose_name_plural': 'Cancelamentos',
            },
        ),
    ]
