from django.forms import inlineformset_factory
from django.shortcuts import render, redirect

from .filters import OrderFilter
from .forms import OrderForm
from .models import Product, Order, Customer


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    pending_orders = orders.filter(status="Pending").count()
    delivered_orders = orders.filter(status="Delivered").count()
    context = {
        "orders": orders,
        "customers": customers,
        "total_orders": total_orders,
        "total_customers": total_customers,
        "pending_orders": pending_orders,
        "delivered_orders": delivered_orders,
    }
    return render(request, context=context, template_name="accounts/dashboard.html")


def products(request):
    products = Product.objects.all()
    return render(
        request, template_name="accounts/products.html", context={"products": products,}
    )


def customers(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()

    # filters are really powerful this allows us to create a very quick 'search'
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    context = {
        "customer": customer,
        "orders": orders,
        "order_count": order_count,
        "myFilter": myFilter,
    }
    return render(request, template_name="accounts/customer.html", context=context)


def create_order(request, pk):
    """
    In this example we do create on a ModelForm which we can
    call .save() on as it maps to the model is sync'd with.
    """
    customer = Customer.objects.get(id=pk)
    OrderedFormSet = inlineformset_factory(
        Customer,
        Order,
        fields=("product", "status"),
        extra=6,  # dictates how many fields to render
    )
    if request.method == "POST":
        formset = OrderedFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect("home")
    else:
        formset = OrderedFormSet(
            queryset=Order.objects.none(), instance=customer  # qs none() return none
        )  # return customer objects
    #     form = OrderForm(initial={"customer": customer})
    context = {"formset": formset}

    return render(request, context=context, template_name="accounts/order_form.html")


def update_order(request, pk):
    """
    Updates to an object are done by accessing the objects id via the
    pk variable and then setting the form to map its values against
    that id with `instance=order`.
    """
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = OrderForm(instance=order)
    context = {"form": form}
    return render(request, context=context, template_name="accounts/order_form.html")


def delete_order(request, pk):
    """
    To delete an item using a form we again pass in the pk to retrieve it
    via the ORM. This gives access to the delete method on the object.
    In the form html, we reference the item and its attributes for user
    view port.
    """
    item = Order.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("home")
    context = {"item": item}
    return render(request, "accounts/delete.html", context=context)
