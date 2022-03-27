from rest_framework.relations import PrimaryKeyRelatedField, StringRelatedField
from rest_framework.serializers import ModelSerializer
from ..models import Servico, CategoriaServico
from rest_framework import serializers

# Create models serializers
class ServicesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    contato_servico = serializers.CharField(max_length=255)

    categoria = StringRelatedField()

