from django.shortcuts import render
from ..models import Servico
from ..api.serializers import ServicesSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


'''
https://www.youtube.com/watch?v=-x_Z_V9HXZE
https://www.youtube.com/watch?v=Hi3TA2pGv7Y&list=PLmDLs7JbXWNjr5vyJhfGu69sowgIUl8z5&index=15
'''

class ServicesViewSet(viewsets.ModelViewSet):
    serializer_class = ServicesSerializer

    def get_queryset(self):
        services = Servico.objects.all()
        return services

    def get(self, request, *args, **kwargs):
        service = self.get_queryset()
        serializer = ServicesSerializer(service, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        service_data = request.data
        new_service = Servico.objects.create(
            contato_servico = service_data['Rosivaldo de Jesus'],
            endereco_servico=service_data['Em algum lugar qualquer']
        )
        new_service.save()
        serializer = ServicesSerializer(new_service)
        return Response(serializer.data)






    # def ListaServico(request):
    #     if request.method == 'GET':
    #         servico = Servico.objects.all()
    #         serializer = ServicesSerializer(servico, many=True)
    #         return Response(serializer.data)





# @api_view(['GET'])
#     def ListaServico(request):
#         if request.method == 'GET':
#             servico = Servico.objects.all()
#             serializer = ServicesSerializer(servico, many=True)
#             return Response(serializer.data)
#

# class ServicesViewSet(ModelViewSet):
#     queryset = Servico.objects.all()[:10]
#     serializer_class = ServicesSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    # Método de localizar por filtros
    # filter_backends = [SearchFilter]
    # filterset_fields = ['id', 'contato_servico']

    # Método de localizar por pesquisa(search)
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['id', 'contato_servico']


    # def get_queryset(self):
    #     return Servico.objects.filter()
    #
    # def list(self, request, *args, **kwargs):
    #     pass
    #     # return Response({'teste': 123})
    #
    # def create(self, request, *args, **kwargs):
    #     pass
    #     #return Response({'Hello': request.data['Rosivaldo']})
    #
    # def destroy(self, request, *args, **kwargs):
    #     pass
    #
    # def retrieve(self, request, *args, **kwargs):
    #     pass
    #
    # def update(self, request, *args, **kwargs):
    #     pass
    #
    # def partial_update(self, request, *args, **kwargs):
    #     pass
    #
