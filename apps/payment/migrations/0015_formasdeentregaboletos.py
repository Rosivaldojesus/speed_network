# Generated by Django 3.0 on 2021-11-09 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0014_entregaboletos'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormasDeEntregaBoletos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma_entrega', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Formas Entrega Boletos',
            },
        ),
    ]
