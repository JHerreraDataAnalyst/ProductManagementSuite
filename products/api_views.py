from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q, F
from django.db import models
from .models import Product, Category
from .serializers import ProductListSerializer, ProductDetailSerializer, CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        return ProductListSerializer
    
    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)
        
        # Filtros
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category_id=category)
        
        min_stock = self.request.query_params.get('min_stock')
        if min_stock:
            queryset = queryset.filter(stock_quantity__gte=min_stock)
        
        max_stock = self.request.query_params.get('max_stock')
        if max_stock:
            queryset = queryset.filter(stock_quantity__lte=max_stock)
        
        return queryset
    
    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')
        barcode = request.query_params.get('barcode', '')
        
        if barcode:
            products = Product.objects.filter(barcode=barcode, is_active=True)
        elif query:
            products = Product.objects.filter(
                Q(name__icontains=query) |
                Q(sku__icontains=query) |
                Q(description__icontains=query),
                is_active=True
            )
        else:
            return Response({"error": "Proporciona parámetro 'q' o 'barcode'"}, status=400)
        
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        low_stock_products = Product.objects.filter(
            stock_quantity__lte=F('min_stock'),
            is_active=True
        )
        serializer = self.get_serializer(low_stock_products, many=True)
        return Response(serializer.data)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer