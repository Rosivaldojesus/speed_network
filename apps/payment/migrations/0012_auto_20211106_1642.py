# Generated by Django 3.0 on 2021-11-06 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0009_bancos'),
        ('payment', '0011_bancos'),
    ]

    operations = [
        migrations.CreateModel(
            name='DestinoValoresBoletos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('data_transacao', models.DateField(blank=True, null=True)),
                ('data_cadastro', models.DateTimeField(auto_now=True)),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='components.Bancos')),
            ],
            options={
                'verbose_name_plural': 'Destino Valores Boletos',
            },
        ),
        migrations.DeleteModel(
            name='Bancos',
        ),
    ]
