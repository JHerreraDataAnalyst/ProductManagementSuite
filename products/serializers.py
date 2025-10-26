from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'product_count', 'created_at']
    
    def get_product_count(self, obj):
        return obj.product_set.count()

class ProductListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    stock_status = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'sku', 'barcode', 'category', 'category_name',
            'price', 'cost', 'stock_quantity', 'min_stock', 'stock_status',
            'profit_margin', 'is_active'
        ]
    
    def get_stock_status(self, obj):
        if obj.stock_quantity == 0:
            return 'out-of-stock'
        elif obj.stock_quantity <= obj.min_stock:
            return 'low-stock'
        else:
            return 'in-stock'

class ProductDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Product
        fields = '__all__'