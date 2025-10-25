from django.shortcuts import render
from django.db.models import Sum, Count, F
from django.utils import timezone
from datetime import timedelta
from products.models import Product
from sales.models import Sale
from clients.models import Client

def dashboard(request):
    try:
        # Estadísticas principales
        total_products = Product.objects.count()
        
        # Productos con stock bajo
        low_stock_products = Product.objects.filter(
            stock_quantity__lte=F('min_stock')
        ).count()
        
        total_clients = Client.objects.count()
        
        # Ventas del mes
        start_of_month = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        monthly_sales = Sale.objects.filter(
            sale_date__gte=start_of_month
        ).aggregate(
            total_sales=Sum('total'),
            sales_count=Count('id')
        )
        
        # Productos más vendidos (simplificado por ahora)
        # Como la relación SaleItem puede no tener datos, usamos un enfoque más simple
        top_products = Product.objects.filter(is_active=True).order_by('-stock_quantity')[:5]
        
        context = {
            'total_products': total_products,
            'low_stock_products': low_stock_products,
            'total_clients': total_clients,
            'monthly_revenue': monthly_sales['total_sales'] or 0,
            'monthly_sales_count': monthly_sales['sales_count'] or 0,
            'top_products': top_products,
        }
        
    except Exception as e:
        # En caso de error, usar valores por defecto
        context = {
            'total_products': 0,
            'low_stock_products': 0,
            'total_clients': 0,
            'monthly_revenue': 0,
            'monthly_sales_count': 0,
            'top_products': [],
        }
    
    return render(request, 'dashboard/dashboard.html', context)