
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from apps.services.api.viewsets import ServicesListViewSet


# As urls das api
router = routers.DefaultRouter()
router.register(r'lista-servicos-api', ServicesListViewSet)




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


    path('api/', include(router.urls)),


]
