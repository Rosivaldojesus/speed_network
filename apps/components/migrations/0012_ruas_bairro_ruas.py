# Generated by Django 3.0 on 2022-02-06 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0011_auto_20211212_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='ruas',
            name='bairro_ruas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='components.Bairros'),
        ),
    ]
