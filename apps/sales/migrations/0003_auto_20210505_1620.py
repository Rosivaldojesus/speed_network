# Generated by Django 3.0 on 2021-05-05 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_instalacao_agendado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instalacao',
            old_name='agendado',
            new_name='data_agendada',
        ),
    ]
