# Generated by Django 3.0 on 2021-08-23 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voip', '0003_servicovoip_observacao_instalacao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicovoip',
            old_name='observacao_instalacao',
            new_name='observacao_voip',
        ),
    ]
