# Generated by Django 3.0 on 2021-07-12 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cto', '0008_ponporcaixaemenda_numero_pon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ponporcaixaemenda',
            name='numero_pon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cto.CaixasDeEmenda'),
        ),
    ]
