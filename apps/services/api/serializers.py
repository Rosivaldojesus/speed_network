from rest_framework.serializers import ModelSerializer
from ..models import Servico

# Create models serializers
class ServicesSerializer(ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'