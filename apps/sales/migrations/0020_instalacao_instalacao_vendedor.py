# Generated by Django 3.0 on 2021-06-09 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0006_vendedores'),
        ('sales', '0019_auto_20210527_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='instalacao',
            name='instalacao_vendedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Vendedor', to='components.Vendedores'),
        ),
    ]
