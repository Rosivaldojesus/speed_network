from rest_framework.viewsets import ModelViewSet
from ..api.serializers import ServicesSerializer
from ..models import Servico


class ServicesListViewSet(ModelViewSet):
    queryset = Servico.objects.all()[:10]
    serializer_class = ServicesSerializer