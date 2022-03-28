from rest_framework.relations import PrimaryKeyRelatedField, StringRelatedField
from rest_framework.serializers import ModelSerializer
from ..models import Servico, CategoriaServico
from rest_framework import serializers

# Create models serializers
class ServicesSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # contato_servico = serializers.CharField(max_length=255)
    # categoria = StringRelatedField()
    # agendado_por = StringRelatedField()
    # funcionario_servico = StringRelatedField()
    # finalizado_por = StringRelatedField()
    # plano_internet = StringRelatedField()
    # criado_por = StringRelatedField()

    class Meta:
        model = Servico
        fields = ['id', 'contato_servico']

