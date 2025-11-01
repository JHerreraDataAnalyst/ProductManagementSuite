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

# Agrega URLs personalizadas para compatibilidad con tu app móvil
urlpatterns = [
    path('', include(router.urls)),
    
    # URLs compatibles con tu app móvil
    path('products/search/', ProductViewSet.as_view({'get': 'search'}), name='product-search'),
    path('products/low_stock/', ProductViewSet.as_view({'get': 'low_stock'}), name='low-stock'),
    path('sales/today_sales/', SaleViewSet.as_view({'get': 'today_sales'}), name='today-sales'),
    path('sales/quick_sale/', SaleViewSet.as_view({'post': 'quick_sale'}), name='quick-sale'),
    path('sales/top_products/', SaleViewSet.as_view({'get': 'top_products'}), name='top-products'),
    path('clients/search/', ClientViewSet.as_view({'get': 'search'}), name='client-search'),
]