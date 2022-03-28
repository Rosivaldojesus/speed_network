
from django.contrib import admin
from django.urls import path, include




# Imports das API
from rest_framework import routers
from apps.core.api import viewsets
from apps.core.api.viewsets import UserViewSet
from apps.services.api.viewsets import ServicesViewSet
from rest_framework.authtoken.views import obtain_auth_token


# As urls das api
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'users',viewsets.UserViewSet)
router.register(r'groups', viewsets.GroupViewSet)

router.register(r'lista-servicos-api', ServicesViewSet, basename='Servico')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('estoque/', include('apps.stock.urls')),
    path('pagamentos/', include('apps.payment.urls')),
    path('vendas/', include('apps.sales.urls')),
    path('servicos/', include('apps.services.urls')),
    path('componentes/', include('apps.components.urls')),
    path('cto/', include('apps.cto.urls')),
    path('voip/', include('apps.voip.urls')),
    path('tarefas/', include('apps.tasks.urls')),

    # Urls das api
    path('api-auth/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('api/', include(router.urls)),



]
