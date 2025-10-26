from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum, Count
from django.utils import timezone
from datetime import timedelta
from .models import Sale, SaleItem
from .serializers import SaleSerializer, QuickSaleSerializer
from products.models import Product  # ✅ CORREGIDO: Importar desde products
# ❌ ELIMINAR: from .models import Product, Category

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all().order_by('-sale_date')
    serializer_class = SaleSerializer
    
    def get_queryset(self):
        queryset = Sale.objects.all().order_by('-sale_date')
        
        # Filtros por fecha
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        
        if start_date:
            queryset = queryset.filter(sale_date__gte=start_date)
        if end_date:
            queryset = queryset.filter(sale_date__lte=end_date)
        
        return queryset
    
    @action(detail=False, methods=['post'])
    def quick_sale(self, request):
        serializer = QuickSaleSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            
            try:
                product = Product.objects.get(id=data['product_id'], is_active=True)
            except Product.DoesNotExist:
                return Response({"error": "Producto no encontrado"}, status=404)
            
            # Verificar stock
            if product.stock_quantity < data['quantity']:
                return Response(
                    {"error": f"Stock insuficiente. Disponible: {product.stock_quantity}"},
                    status=400
                )
            
            # Crear venta
            sale = Sale(
                client_id=data.get('client_id'),
                payment_method=data['payment_method'],
                is_paid=True
            )
            sale.subtotal = product.price * data['quantity']
            sale.save()
            
            # Crear item de venta
            sale_item = SaleItem(
                sale=sale,
                product=product,
                quantity=data['quantity'],
                unit_price=product.price
            )
            sale_item.save()
            
            # Actualizar stock
            product.stock_quantity -= data['quantity']
            product.save()
            
            return Response(SaleSerializer(sale).data, status=201)
        
        return Response(serializer.errors, status=400)
    
    @action(detail=False, methods=['get'])
    def today_sales(self, request):
        today = timezone.now().date()
        sales = Sale.objects.filter(sale_date__date=today)
        serializer = self.get_serializer(sales, many=True)
        
        total_sales = sales.count()
        total_revenue = sales.aggregate(total=Sum('total'))['total'] or 0
        
        return Response({
            'sales': serializer.data,
            'summary': {
                'total_sales': total_sales,
                'total_revenue': total_revenue,
                'date': today
            }
        })
    
    @action(detail=False, methods=['get'])
    def top_products(self, request):
        days = int(request.query_params.get('days', 30))
        start_date = timezone.now() - timedelta(days=days)
        
        top_products = SaleItem.objects.filter(
            sale__sale_date__gte=start_date
        ).values(
            'product__id', 'product__name', 'product__sku'
        ).annotate(
            total_sold=Sum('quantity'),
            total_revenue=Sum('total_price')
        ).order_by('-total_sold')[:10]
        
        return Response(top_products)