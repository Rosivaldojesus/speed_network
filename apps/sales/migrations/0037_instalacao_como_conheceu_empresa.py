# Generated by Django 3.0 on 2021-10-26 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0036_cancelamentos_motivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='instalacao',
            name='como_conheceu_empresa',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]