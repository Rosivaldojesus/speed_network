# Generated by Django 3.0 on 2021-11-09 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0012_auto_20211106_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormasEntregaBoletos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma_entrega', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Formas Entrega Boletos',
            },
        ),
    ]
