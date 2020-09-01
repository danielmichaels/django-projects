from django.contrib import messages
from django.shortcuts import render, redirect

from users.forms import UserRegisterForm


def register(request):
    """
    User registration.
    """
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Sign Up Confirmed, Welcome {username}")
            return redirect("blog-home")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", context={"form": form})
