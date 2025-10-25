from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Client
from .forms import ClientForm

def client_list(request):
    # Filtros y búsqueda
    query = request.GET.get('q', '')
    client_type = request.GET.get('type', '')
    
    clients = Client.objects.all()
    
    if query:
        clients = clients.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(company_name__icontains=query) |
            Q(email__icontains=query) |
            Q(tax_id__icontains=query)
        )
    
    if client_type:
        clients = clients.filter(type=client_type)
    
    # Paginación
    paginator = Paginator(clients, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'clients': page_obj,
        'page_obj': page_obj,
        'query': query,
        'client_type': client_type,
    }
    return render(request, 'clients/client_list.html', context)

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    
    context = {
        'client': client,
    }
    return render(request, 'clients/client_detail.html', context)

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            messages.success(request, f'Cliente "{client.full_name}" creado exitosamente.')
            return redirect('clients:client_detail', pk=client.pk)
    else:
        form = ClientForm()
    
    context = {
        'form': form,
        'title': 'Crear Cliente',
    }
    return render(request, 'clients/client_form.html', context)

def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save()
            messages.success(request, f'Cliente "{client.full_name}" actualizado exitosamente.')
            return redirect('clients:client_detail', pk=client.pk)
    else:
        form = ClientForm(instance=client)
    
    context = {
        'form': form,
        'title': 'Editar Cliente',
        'client': client,
    }
    return render(request, 'clients/client_form.html', context)

def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    
    if request.method == 'POST':
        client_name = client.full_name
        client.delete()
        messages.success(request, f'Cliente "{client_name}" eliminado exitosamente.')
        return redirect('clients:client_list')
    
    context = {
        'client': client,
    }
    return render(request, 'clients/client_confirm_delete.html', context)