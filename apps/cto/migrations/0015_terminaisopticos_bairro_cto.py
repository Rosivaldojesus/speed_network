# Generated by Django 3.0 on 2021-11-29 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0010_bairros'),
        ('cto', '0014_caixasdasprimarias_primaria'),
    ]

    operations = [
        migrations.AddField(
            model_name='terminaisopticos',
            name='bairro_cto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='components.Bairros'),
        ),
    ]
