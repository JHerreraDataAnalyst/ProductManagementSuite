from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.api_views import ProductViewSet, CategoryViewSet
from sales.api_views import SaleViewSet
from clients.api_views import ClientViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]