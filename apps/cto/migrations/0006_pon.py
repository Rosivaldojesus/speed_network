# Generated by Django 3.0 on 2021-07-12 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cto', '0005_ponporcaixaemenda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoPon', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True)),
            ],
            options={
                'verbose_name_plural': 'PON',
            },
        ),
    ]
