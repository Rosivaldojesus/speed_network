from ..models import Servico

from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows services to be viewed or edited.
    """
    queryset = Servico.objects.all()
    serializer_class = ServiceSerializer
    #permission_classes = [permissions.IsAuthenticated]
    #authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]