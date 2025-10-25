from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q, Sum
from django.core.paginator import Paginator
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Sale, SaleItem
from .forms import SaleForm, SaleItemFormSet
from clients.models import Client
from products.models import Product

def sale_list(request):
    # Filtros y búsqueda
    query = request.GET.get('q', '')
    date_from = request.GET.get('date_from', '')
    date_to = request.GET.get('date_to', '')
    
    sales = Sale.objects.all().order_by('-sale_date')
    
    if query:
        sales = sales.filter(
            Q(client__first_name__icontains=query) |
            Q(client__last_name__icontains=query) |
            Q(client__company_name__icontains=query) |
            Q(id__icontains=query)
        )
    
    if date_from:
        try:
            date_from = datetime.strptime(date_from, '%Y-%m-%d')
            sales = sales.filter(sale_date__gte=date_from)
        except ValueError:
            pass
    
    if date_to:
        try:
            date_to = datetime.strptime(date_to, '%Y-%m-%d')
            sales = sales.filter(sale_date__lte=date_to)
        except ValueError:
            pass
    
    # Paginación
    paginator = Paginator(sales, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Estadísticas
    total_sales = sales.count()
    total_revenue = sales.aggregate(total=Sum('total'))['total'] or 0
    
    context = {
        'sales': page_obj,
        'page_obj': page_obj,
        'query': query,
        'date_from': date_from,
        'date_to': date_to,
        'total_sales': total_sales,
        'total_revenue': total_revenue,
    }
    return render(request, 'sales/sale_list.html', context)

def sale_detail(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    items = sale.items.all()
    
    context = {
        'sale': sale,
        'items': items,
    }
    return render(request, 'sales/sale_detail.html', context)

def sale_create(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        formset = SaleItemFormSet(request.POST)
        
        if form.is_valid() and formset.is_valid():
            sale = form.save(commit=False)
            sale.subtotal = 0
            sale.save()
            
            # Calcular subtotal de los items
            subtotal = 0
            for form in formset:
                if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                    sale_item = form.save(commit=False)
                    sale_item.sale = sale
                    sale_item.unit_price = sale_item.product.price
                    sale_item.save()
                    subtotal += sale_item.total_price
            
            # Actualizar sale con subtotal y total
            sale.subtotal = subtotal
            sale.save()
            
            messages.success(request, f'Venta #{sale.id} creada exitosamente.')
            return redirect('sales:sale_detail', pk=sale.pk)
    else:
        form = SaleForm()
        formset = SaleItemFormSet()
    
    context = {
        'form': form,
        'formset': formset,
        'title': 'Crear Venta',
        'clients': Client.objects.all(),
        'products': Product.objects.filter(is_active=True),
    }
    return render(request, 'sales/sale_form.html', context)

def sale_update(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    
    if request.method == 'POST':
        form = SaleForm(request.POST, instance=sale)
        formset = SaleItemFormSet(request.POST, instance=sale)
        
        if form.is_valid() and formset.is_valid():
            sale = form.save(commit=False)
            sale.subtotal = 0
            sale.save()
            
            # Recalcular subtotal
            subtotal = 0
            for form in formset:
                if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                    sale_item = form.save(commit=False)
                    sale_item.sale = sale
                    if not sale_item.unit_price:
                        sale_item.unit_price = sale_item.product.price
                    sale_item.save()
                    subtotal += sale_item.total_price
            
            sale.subtotal = subtotal
            sale.save()
            
            messages.success(request, f'Venta #{sale.id} actualizada exitosamente.')
            return redirect('sales:sale_detail', pk=sale.pk)
    else:
        form = SaleForm(instance=sale)
        formset = SaleItemFormSet(instance=sale)
    
    context = {
        'form': form,
        'formset': formset,
        'title': 'Editar Venta',
        'sale': sale,
        'clients': Client.objects.all(),
        'products': Product.objects.filter(is_active=True),
    }
    return render(request, 'sales/sale_form.html', context)

def sale_delete(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    
    if request.method == 'POST':
        sale_id = sale.id
        sale.delete()
        messages.success(request, f'Venta #{sale_id} eliminada exitosamente.')
        return redirect('sales:sale_list')
    
    context = {
        'sale': sale,
    }
    return render(request, 'sales/sale_confirm_delete.html', context)