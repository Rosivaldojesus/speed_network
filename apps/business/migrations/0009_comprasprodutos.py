# Generated by Django 3.0 on 2022-06-07 18:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business', '0008_auto_20220601_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComprasProdutos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=200, verbose_name='Nome do Produto')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
                ('valor_unitario', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor Unitário')),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor Total')),
                ('concluido', models.BooleanField(default=False, verbose_name='Concluído')),
                ('data_criacao', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data da Criação')),
                ('ultima_alteracao', models.DateTimeField(auto_now=True, verbose_name='Data da Última Alteração')),
                ('data_concluido', models.DateTimeField(auto_now=True, verbose_name='Data da Conclusão')),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Observação')),
                ('concluido_por', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='c_concluido_por', to=settings.AUTH_USER_MODEL)),
                ('criado_por', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='c_criado_por', to=settings.AUTH_USER_MODEL)),
                ('ultima_alteracao_por', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='c_ultima_alteracao_por', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Compra de Produto',
                'verbose_name_plural': 'Compra de Produtos',
            },
        ),
    ]
