from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField(default=0)
    min_stock = models.IntegerField(default=10)
    sku = models.CharField(max_length=50, unique=True)
    barcode = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='products/', blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def profit_margin(self):
        """Margen de ganancia porcentual (CORREGIDO)"""
        if self.cost > 0:
            return ((self.price - self.cost) / self.cost) * 100
        return 0

    @property
    def stock_status(self):
        """Estado del stock"""
        if self.stock_quantity == 0:
            return "out-of-stock"
        elif self.stock_quantity <= self.min_stock:
            return "low-stock"
        else:
            return "in-stock"

    @property
    def total_stock_value(self):
        """Valor total del stock (costo * cantidad)"""
        return float(self.cost) * self.stock_quantity
    
    @property
    def potential_profit(self):
        """Ganancia potencial total (margen * cantidad)"""
        return float(self.price - self.cost) * self.stock_quantity

    @property
    def is_low_stock(self):
        """¿El stock está bajo?"""
        return self.stock_quantity <= self.min_stock

    @property
    def is_out_of_stock(self):
        """¿Está agotado?"""
        return self.stock_quantity == 0

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-created_at']