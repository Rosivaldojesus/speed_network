# Generated by Django 3.0 on 2021-11-29 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0009_bancos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bairros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_bairro', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Bairros',
            },
        ),
    ]
