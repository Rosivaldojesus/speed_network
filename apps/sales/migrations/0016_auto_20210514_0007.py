# Generated by Django 3.0 on 2021-05-14 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0015_auto_20210514_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instalacao',
            name='data_concluido',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]