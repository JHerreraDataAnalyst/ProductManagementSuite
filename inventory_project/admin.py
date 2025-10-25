from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from products.models import Product, Category
from clients.models import Client
from products.models import Sale, SaleItem

# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'type', 'email', 'phone', 'city', 'created_at')
    list_filter = ('type', 'city', 'country', 'created_at')
    search_fields = ('first_name', 'last_name', 'company_name', 'email', 'tax_id')
    list_per_page = 20

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_count', 'created_at')
    search_fields = ('name', 'description')
    
    def product_count(self, obj):
        return obj.product_set.count()
    product_count.short_description = 'Productos'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'cost', 'stock_quantity', 'stock_status_badge', 'is_active')
    list_filter = ('category', 'is_active', 'created_at')
    search_fields = ('name', 'sku', 'barcode')
    list_editable = ('price', 'stock_quantity', 'is_active')
    list_per_page = 25
    
    def stock_status_badge(self, obj):
        status = obj.stock_status
        colors = {
            'out-of-stock': 'danger',
            'low-stock': 'warning',
            'in-stock': 'success'
        }
        return format_html(
            '<span class="badge bg-{}">{}</span>',
            colors[status],
            status.upper()
        )
    stock_status_badge.short_description = 'Estado Stock'

class SaleItemInline(admin.TabularInline):
    model = SaleItem
    extra = 1
    readonly_fields = ('total_price',)

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'sale_date', 'total', 'payment_method', 'is_paid')
    list_filter = ('sale_date', 'payment_method', 'is_paid')
    search_fields = ('client__first_name', 'client__last_name', 'client__company_name')
    inlines = [SaleItemInline]
    readonly_fields = ('subtotal', 'tax', 'total', 'created_at')
    list_per_page = 20