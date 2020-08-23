from django.shortcuts import render


def home(request):
    return render(request, template_name="accounts/dashboard.html")


def products(request):
    return render(request, template_name="accounts/products.html")


def customers(request):
    return render(request, template_name="accounts/customer.html")
