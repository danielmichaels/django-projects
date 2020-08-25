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
]
