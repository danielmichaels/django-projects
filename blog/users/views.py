from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
            messages.success(request, f"Sign Up Confirmed, Welcome {username}, Please Login")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", context={"form": form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
