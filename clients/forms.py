from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['type', 'first_name', 'last_name', 'company_name', 'email', 
                 'phone', 'address', 'city', 'country', 'tax_id', 'notes']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control', 'id': 'client-type'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Razón Social (para empresas)'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+1234567890'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Dirección completa'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'País'}),
            'tax_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RUC/Cédula'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Notas adicionales'}),
        }
        labels = {
            'type': 'Tipo de Cliente',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'company_name': 'Razón Social',
            'email': 'Correo Electrónico',
            'phone': 'Teléfono',
            'address': 'Dirección',
            'city': 'Ciudad',
            'country': 'País',
            'tax_id': 'RUC/Cédula',
            'notes': 'Notas',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Client.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Este email ya está registrado.")
        return email