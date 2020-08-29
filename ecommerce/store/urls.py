from django.urls import path

from store import views

urlpatterns = [
    path("", views.store, name="store"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    # JSON
    path("update_item/", views.update_item, name="update_item"),
    path("process_order/", views.process_order, name="process_order"),
]
