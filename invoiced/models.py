from django.db import models

# Create your models here.

class Invoice(models.Model):
    invoice = models.FileField(upload_to='invoices/')
    invoice_number = models.CharField(max_length=200)
    client_number = models.CharField(max_length=200)
    date_of_scanning = models.CharField(max_length=200)
    date_of_upload = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.invoice_number
