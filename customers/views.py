from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CustomerForm()
    return render(request, 'customers/form.html', {'form': form})

def success_view(request):
    return render(request, 'customers/success.html')

def list_customers(request):
    q = request.GET.get('q')
    if q:
        customers = Customer.objects.filter(
            models.Q(first_name__icontains=q) | 
            models.Q(last_name__icontains=q) | 
            models.Q(email__icontains=q)
        )
    else:
        customers = Customer.objects.all()

    customers = Customer.objects.all()
    return render(request, 'customers/list.html', {'customers': customers})

def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'customers/form.html', {'form': form})

def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('list')
