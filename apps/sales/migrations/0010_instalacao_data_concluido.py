# Generated by Django 3.0 on 2021-05-08 13:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0009_auto_20210508_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='instalacao',
            name='data_concluido',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
