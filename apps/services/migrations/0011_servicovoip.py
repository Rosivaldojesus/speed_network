# Generated by Django 3.0 on 2021-06-01 00:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0010_servico_finalizado_por'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicoVoip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_usuario_voip', models.CharField(blank=True, max_length=255, null=True, verbose_name='Cliente Voip')),
                ('cpf_usuario_voip', models.CharField(blank=True, max_length=50, null=True, verbose_name='CPF')),
                ('usuario_voip', models.CharField(blank=True, max_length=200, null=True, verbose_name='Usuário Voip')),
                ('Senha_voip', models.CharField(blank=True, max_length=50, null=True, verbose_name='Senha Voip')),
                ('reservado_voip', models.BooleanField(default=False, verbose_name='Reservado')),
                ('data_reserva_voip', models.DateField(blank=True, null=True, verbose_name='Data da Reserva')),
                ('finalizado_voip', models.BooleanField(default=False, verbose_name='Finalizado')),
                ('funcionario_reserva_voip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='funcionário_reserva_voip', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Serviço Vopi',
            },
        ),
    ]
