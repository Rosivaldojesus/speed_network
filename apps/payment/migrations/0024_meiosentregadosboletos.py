# Generated by Django 3.0 on 2021-11-10 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0023_auto_20211110_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeiosEntregaDosBoletos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma_entrega', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Formas Entrega Boletos',
            },
        ),
    ]
