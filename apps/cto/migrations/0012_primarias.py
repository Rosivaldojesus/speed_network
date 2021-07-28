# Generated by Django 3.0 on 2021-07-24 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cto', '0011_auto_20210712_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Primarias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('pon', models.CharField(blank=True, max_length=10, null=True)),
                ('localizacao', models.CharField(blank=True, max_length=255, null=True)),
                ('quant_caixas', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
            ],
            options={
                'verbose_name_plural': 'Primárias',
            },
        ),
    ]