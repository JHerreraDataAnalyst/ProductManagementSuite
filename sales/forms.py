from django import forms
from .models import Sale, SaleItem
from clients.models import Client
from products.models import Product

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['client', 'payment_method', 'is_paid', 'notes']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
            'is_paid': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'client': 'Cliente',
            'payment_method': 'Método de Pago',
            'is_paid': '¿Pagado?',
            'notes': 'Notas',
        }

class SaleItemForm(forms.ModelForm):
    class Meta:
        model = SaleItem
        fields = ['product', 'quantity']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control product-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
        }
        labels = {
            'product': 'Producto',
            'quantity': 'Cantidad',
        }

SaleItemFormSet = forms.inlineformset_factory(
    Sale, 
    SaleItem, 
    form=SaleItemForm,
    extra=1,
    can_delete=True
)