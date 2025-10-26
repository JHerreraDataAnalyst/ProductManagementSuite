from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls', namespace='dashboard')),
    path('products/', include('products.urls', namespace='products')),
    path('clients/', include('clients.urls', namespace='clients')),
    path('sales/', include('sales.urls', namespace='sales')),
    path('api/', include('api.urls')),  # ← NUEVA LÍNEA
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)