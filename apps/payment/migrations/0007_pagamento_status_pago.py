# Generated by Django 3.0 on 2021-05-27 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_agendapagamento_status_pago'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagamento',
            name='status_pago',
            field=models.BooleanField(default=False, verbose_name='Pago'),
        ),
    ]