
from django.contrib import admin
from django.urls import path, include

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


]
