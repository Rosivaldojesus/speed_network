# Generated by Django 3.0 on 2021-05-13 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0012_auto_20210512_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instalacao',
            name='data_concluido',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
