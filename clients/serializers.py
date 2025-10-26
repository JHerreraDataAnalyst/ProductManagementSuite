from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    total_purchases = serializers.SerializerMethodField()
    
    class Meta:
        model = Client
        fields = [
            'id', 'type', 'first_name', 'last_name', 'company_name', 'full_name',
            'email', 'phone', 'address', 'city', 'country', 'tax_id', 'notes',
            'total_purchases', 'created_at'
        ]
    
    def get_total_purchases(self, obj):
        return obj.sales.count()