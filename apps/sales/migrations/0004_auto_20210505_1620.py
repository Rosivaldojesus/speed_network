# Generated by Django 3.0 on 2021-05-05 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_auto_20210505_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instalacao',
            old_name='data_agendada',
            new_name='status_agendada',
        ),
    ]
