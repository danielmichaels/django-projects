from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(views_func):
    """
    If a user is unauthenticated redirect, if authenticated
    but accessing a page they aren't allowed to go to redirect
    """

    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return views_func(request, *args, **kwargs)

    return wrapper


def allowed_user(allowed_roles=None):
    """
    Only allow certain user groups access to views.

    :param allowed_roles: set the roles allowed to access page
    """
    if allowed_roles is None:
        allowed_roles = []

    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                for group in request.user.groups.all():
                    group = group.name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("Not Authorized <a href='/'>Home</a>")

        return wrapper

    return decorator

def admin_only(view_func):
    """
    Admin only decorator for simpler route protections
    """
    def wrapper(request, *args,**kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all().first().name

        if group == 'customer':
            return redirect('user')
        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper
