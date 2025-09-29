from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage
from xhtml2pdf import pisa
from io import BytesIO
from .models import Product
from .forms import ProductForm

def home(request):
    return render(request, 'home.html')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def product_pdf(request, pk):
    product = get_object_or_404(Product, pk=pk)
    template = get_template('product_pdf.html')
    html = template.render({'product': product})
    result = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=result)
    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)
    response = HttpResponse(result.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{product.name}.pdf"'
    return response

def send_product_email(request, pk):
    product = get_object_or_404(Product, pk=pk)
    subject = f'Product Info: {product.name}'
    message = f'Name: {product.name}\nDescription: {product.description}\nPrice: {product.price}'
    email = EmailMessage(subject, message, to=['owner_email@example.com'])
    try:
        email.send()
    except Exception as e:
        return HttpResponse(f'Error sending email: {e}')
    return redirect('product_detail', pk=pk)
