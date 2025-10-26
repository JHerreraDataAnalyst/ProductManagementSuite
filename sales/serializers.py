from rest_framework import serializers
from .models import Sale, SaleItem
from products.serializers import ProductListSerializer

class SaleItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_sku = serializers.CharField(source='product.sku', read_only=True)
    
    class Meta:
        model = SaleItem
        fields = ['id', 'product', 'product_name', 'product_sku', 'quantity', 'unit_price', 'total_price']

class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True, read_only=True)
    client_name = serializers.CharField(source='client.full_name', read_only=True)
    
    class Meta:
        model = Sale
        fields = [
            'id', 'client', 'client_name', 'sale_date', 'subtotal', 'tax', 'total',
            'payment_method', 'is_paid', 'notes', 'items', 'created_at'
        ]

class QuickSaleSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)
    client_id = serializers.IntegerField(required=False)
    payment_method = serializers.ChoiceField(choices=Sale.PAYMENT_METHODS, default='cash')