# Generated by Django 3.0 on 2021-11-10 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0024_meiosentregadosboletos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meiosentregadosboletos',
            options={'verbose_name_plural': 'Meios Entrega Boletos'},
        ),
        migrations.CreateModel(
            name='ClientesEntregaDosBoletos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cliente', models.CharField(blank=True, max_length=255, null=True)),
                ('cpf_cliente', models.CharField(blank=True, max_length=50, null=True)),
                ('data_cadastro', models.DateTimeField(auto_now=True)),
                ('meio_entrega', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='payment.MeiosEntregaDosBoletos')),
            ],
            options={
                'verbose_name_plural': 'Entrega de boletos ',
            },
        ),
    ]