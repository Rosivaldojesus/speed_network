
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('estoque/', include('apps.stock.urls')),
    path('instalacao/', include('apps.components.urls')),


]
