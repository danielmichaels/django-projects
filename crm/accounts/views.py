from django.http import HttpResponse


def home(request):
    return HttpResponse("Home")


def products(request):
    return HttpResponse("products")


def customers(request):
    return HttpResponse("customers")
