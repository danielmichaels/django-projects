from django.shortcuts import render

from .models import Product, Order, Customer


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    pending_orders = orders.filter(status='Pending').count()
    delivered_orders = orders.filter(status='Delivered').count()
    context = {
        'orders': orders,
        'customers': customers,
        'total_orders': total_orders,
        'total_customers': total_customers,
        'pending_orders': pending_orders,
        'delivered_orders': delivered_orders,
    }
    return render(request, context=context,
                  template_name="accounts/dashboard.html")


def products(request):
    products = Product.objects.all()
    return render(request, template_name="accounts/products.html", context={
        'products': products,
    })


def customers(request):
    return render(request, template_name="accounts/customer.html")
