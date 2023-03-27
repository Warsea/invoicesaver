from django import forms
from .models import Invoice

class UploadInvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('invoice', 'invoice_number', 'client_number', 'date_of_scanning')
        widgets = {
            "invoice": forms.FileInput(attrs={'class': 'form-control', 'id': 'invoiceFile', 'onchange': 'autoFill()', 'accept':'.pdf,.doc,.docx'}),
            "invoice_number": forms.TextInput(attrs={'class': 'form-control', 'id': 'invoiceNumber'}),
            "client_number": forms.TextInput(attrs={'class': 'form-control', 'id': 'clientNumber'}),
            "date_of_scanning": forms.TextInput(attrs={'class': 'form-control', 'id': 'dateOfScanning'}),
        }


