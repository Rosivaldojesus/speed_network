from rest_framework.relations import StringRelatedField
#from rest_framework.serializers import ModelSerializer
from apps.services.models import Servico
from rest_framework import serializers

# Create models serializers
class ServiceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    contato_servico = serializers.CharField(max_length=255)
    servico_para_executar = serializers.CharField(max_length=255)
    categoria = StringRelatedField()

    # agendado_por = StringRelatedField()
    # funcionario_servico = StringRelatedField()
    # finalizado_por = StringRelatedField()
    # plano_internet = StringRelatedField()
    # criado_por = StringRelatedField()

    class Meta:
        model = Servico
        fields = [
            'id',
            'contato_servico',
            'categoria',
            'servico_para_executar',
            'endereco_servico',
            'data_agendada',
            'hora_agendada',
        ]

