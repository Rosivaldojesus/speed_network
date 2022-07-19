# Generated by Django 3.0 on 2022-06-07 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business', '0009_comprasprodutos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vendasprodutos',
            options={'verbose_name': 'Venda de Produto', 'verbose_name_plural': 'Venda de Produtos'},
        ),
        migrations.AlterField(
            model_name='comprasprodutos',
            name='concluido',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Concluído'),
        ),
        migrations.AlterField(
            model_name='comprasprodutos',
            name='concluido_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='c_concluido_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comprasprodutos',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='c_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comprasprodutos',
            name='data_concluido',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Data da Conclusão'),
        ),
        migrations.AlterField(
            model_name='comprasprodutos',
            name='data_criacao',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Data da Criação'),
        ),
        migrations.AlterField(
            model_name='comprasprodutos',
            name='quantidade',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantidade'),
        ),
        migrations.AlterField(
            model_name='comprasprodutos',
            name='ultima_alteracao_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='c_ultima_alteracao_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comprasprodutos',
            name='valor_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Valor Total'),
        ),
        migrations.AlterField(
            model_name='comprasprodutos',
            name='valor_unitario',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Valor Unitário'),
        ),
    ]