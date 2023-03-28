from django.shortcuts import render, redirect
from .forms import UploadInvoiceForm
from .models import Invoice

from django.http import HttpResponse
def index(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoiced/user_index.html', {"invoices": invoices})


def login(request):
    return render(request, 'invoiced/login.html')


def register(request):
    return render(request, 'invoiced/register.html')

def upload(request):
    if request.method == 'POST':
        form = UploadInvoiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UploadInvoiceForm()
        context =  {"form": form}
        return render(request, 'invoiced/invoice_form.html', context)