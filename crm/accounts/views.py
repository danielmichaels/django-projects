from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect

from .decorators import unauthenticated_user, allowed_user, admin_only
from .filters import OrderFilter
from .forms import OrderForm, CreateUserForm, CustomerForm
from .models import Product, Order, Customer


@login_required(login_url="login")
@admin_only
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


@login_required(login_url="login")
@allowed_user(allowed_roles=["admin"])
def products(request):
    products = Product.objects.all()
    return render(
        request, template_name="accounts/products.html", context={"products": products,}
    )


@login_required(login_url="login")
@allowed_user(allowed_roles=["admin"])
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


@login_required(login_url="login")
@allowed_user(allowed_roles=["admin"])
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


@login_required(login_url="login")
@allowed_user(allowed_roles=["admin"])
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


@login_required(login_url="login")
@allowed_user(allowed_roles=["admin"])
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


@unauthenticated_user
def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request, f"Success! Please Login as {form.cleaned_data.get('username')}"
            )
            return redirect("login")
    else:
        form = CreateUserForm()

    context = {"form": form}
    return render(request, "accounts/register.html", context)


@unauthenticated_user
def login_(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "could not authenticate user")
    context = {}
    return render(request, "accounts/login.html", context)


@login_required(login_url="login")
def logout_(request):
    logout(request)
    return redirect("home")


@allowed_user(allowed_roles=["customer"])
def user(request):
    orders = request.user.customer.order_set.all()
    total_order = orders.count()
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()

    context = {
        "orders": orders,
        "total_orders": total_order,
        "delivered_orders": delivered,
        "pending_orders": pending,
    }
    return render(request, "accounts/user.html", context)


@login_required(login_url="login")
@allowed_user(["customer"])
def account_settings(request):
    customer = request.user.customer
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = CustomerForm(instance=customer)
    context = {'form':form}
    return render(request, "accounts/account_settings.html", context)
