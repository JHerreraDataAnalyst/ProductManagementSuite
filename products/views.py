from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.db import models  # ✅ AGREGAR ESTA IMPORTACIÓN
from .models import Product, Category
from .forms import ProductForm, CategoryForm

def product_list(request):
    # Filtros y búsqueda
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    stock_status = request.GET.get('stock_status', '')
    
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
    
    # Filtro por estado de stock
    if stock_status == 'low':
        products = products.filter(stock_quantity__lte=models.F('min_stock'), stock_quantity__gt=0)
    elif stock_status == 'out':
        products = products.filter(stock_quantity=0)
    elif stock_status == 'normal':
        products = products.filter(stock_quantity__gt=models.F('min_stock'))
    
    # Estadísticas
    total_products = Product.objects.count()
    active_products = Product.objects.filter(is_active=True).count()
    low_stock_count = Product.objects.filter(
        stock_quantity__lte=models.F('min_stock'), 
        stock_quantity__gt=0,
        is_active=True
    ).count()
    out_of_stock_count = Product.objects.filter(stock_quantity=0, is_active=True).count()
    
    # Paginación
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'products': page_obj,
        'page_obj': page_obj,
        'query': query,
        'category_id': category_id,
        'stock_status': stock_status,
        'categories': Category.objects.all(),
        'total_products': total_products,
        'active_products': active_products,
        'low_stock_count': low_stock_count,
        'out_of_stock_count': out_of_stock_count,
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







# Vistas para Categorías
def category_list(request):
    categories = Category.objects.all()
    
    context = {
        'categories': categories,
    }
    return render(request, 'products/category_list.html', context)

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, f'Categoría "{category.name}" creada exitosamente.')
            return redirect('products:category_list')
    else:
        form = CategoryForm()
    
    context = {
        'form': form,
        'title': 'Crear Categoría',
    }
    return render(request, 'products/category_form.html', context)

def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            messages.success(request, f'Categoría "{category.name}" actualizada exitosamente.')
            return redirect('products:category_list')
    else:
        form = CategoryForm(instance=category)
    
    context = {
        'form': form,
        'title': 'Editar Categoría',
        'category': category,
    }
    return render(request, 'products/category_form.html', context)

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    
    if request.method == 'POST':
        category_name = category.name
        # Verificar si hay productos usando esta categoría
        product_count = Product.objects.filter(category=category).count()
        if product_count > 0:
            messages.error(request, f'No se puede eliminar la categoría "{category_name}" porque tiene {product_count} productos asociados.')
            return redirect('products:category_list')
        
        category.delete()
        messages.success(request, f'Categoría "{category_name}" eliminada exitosamente.')
        return redirect('products:category_list')
    
    context = {
        'category': category,
    }
    return render(request, 'products/category_confirm_delete.html', context)