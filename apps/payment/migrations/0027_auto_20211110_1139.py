# Generated by Django 3.0 on 2021-11-10 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0026_auto_20211110_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientesentregadosboletos',
            name='meio_entrega',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='payment.MeiosEntregaDosBoletos'),
        ),
    ]
