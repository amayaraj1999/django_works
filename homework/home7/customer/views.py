from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm

# Add customer
def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_customers')
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})

# Show all customers
def all_customers(request):
    customers = Customer.objects.all().order_by('name')
    return render(request, 'all_customers.html', {'customers': customers})

# Show filtered customers
def filtered_customers(request):
    customers = Customer.objects.filter(email__endswith='@example.com').order_by('name')
    return render(request, 'filtered_customers.html', {'customers': customers})
