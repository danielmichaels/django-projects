from django.contrib.auth import views as auth_views
from django.urls import path

from accounts import views

urlpatterns = [
    # name='xyz' means we can reference it as {% url 'customer' %} in
    # a template
    path("", views.home, name="home"),
    path("products/", views.products, name="products"),
    path("customer/<str:pk>/", views.customers, name="customer"),
    # CRUD
    path("create_order/<str:pk>/", views.create_order, name="create_order"),
    path("update_order/<str:pk>/", views.update_order, name="update_order"),
    path("delete_order/<str:pk>/", views.delete_order, name="delete_order"),
    # AUTHENTICATION
    path("login/", views.login_, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_, name="logout"),
    # USERS
    path("user/", views.user, name="user"),
    path("account/", views.account_settings, name="account"),
    # DJANGO AUTH VIEWS
    # how to customise your own django auth forms
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(
            template_name="accounts/resets/password_reset.html"
        ),
        name="reset_password",
    ),
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/resets/password_reset_sent.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/resets/password_reset_form.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/resets/password_reset_done.html"
        ),
        name="password_reset_complete",
    ),
]
