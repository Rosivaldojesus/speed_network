
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import  static

# Imports das API
from rest_framework import routers
from apps.services.api.viewsets import ServiceViewSet

router = routers.DefaultRouter()

# Sempre colocar o basename
router.register(r'servicos', ServiceViewSet, basename='servicos')


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

    #Paths of the api´s
    path('api/', include(router.urls)),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
