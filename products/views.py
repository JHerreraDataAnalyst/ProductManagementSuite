from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Product, Category
from .forms import ProductForm

def product_list(request):
    # Filtros y búsqueda
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    
    products = Product.objects.filter(is_active=True)
    
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(sku__icontains=query) |
            Q(barcode__icontains=query) |
            Q(description__icontains=query)
        )
    
    if category_id:
        products = products.filter(category_id=category_id)
    
    # Paginación
    paginator = Paginator(products, 10)  # 10 productos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'products': page_obj,
        'page_obj': page_obj,
        'query': query,
        'category_id': category_id,
        'categories': Category.objects.all(),  # Cambio aquí
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    # Calcular métricas usando la propiedad que ya tienes en el modelo
    profit_margin = product.profit_margin
    
    context = {
        'product': product,
        'profit_margin': round(profit_margin, 2),
    }
    return render(request, 'products/product_detail.html', context)

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Agregar request.FILES para la imagen
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Producto "{product.name}" creado exitosamente.')
            return redirect('products:product_detail', pk=product.pk)
    else:
        form = ProductForm()
    
    context = {
        'form': form,
        'title': 'Crear Producto',
    }
    return render(request, 'products/product_form.html', context)

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)  # Agregar request.FILES
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Producto "{product.name}" actualizado exitosamente.')
            return redirect('products:product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    
    context = {
        'form': form,
        'title': 'Editar Producto',
        'product': product,
    }
    return render(request, 'products/product_form.html', context)

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        product_name = product.name
        # En lugar de eliminar físicamente, marcamos como inactivo
        product.is_active = False
        product.save()
        messages.success(request, f'Producto "{product_name}" eliminado exitosamente.')
        return redirect('products:product_list')
    
    context = {
        'product': product,
    }
    return render(request, 'products/product_confirm_delete.html', context)