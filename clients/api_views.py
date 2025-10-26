from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Client
from .serializers import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', '')
        
        if query:
            clients = Client.objects.filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query) |
                Q(company_name__icontains=query) |
                Q(email__icontains=query) |
                Q(tax_id__icontains=query)
            )
        else:
            return Response({"error": "Proporciona parámetro 'q'"}, status=400)
        
        serializer = self.get_serializer(clients, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def purchase_history(self, request, pk=None):
        client = self.get_object()
        sales = client.sales.all().order_by('-sale_date')
        
        # Usamos el serializer de ventas
        from sales.serializers import SaleSerializer
        serializer = SaleSerializer(sales, many=True)
        
        return Response(serializer.data)