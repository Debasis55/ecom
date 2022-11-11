from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("checkout", views.checkout, name="checkout"),
    path("cart",views.cart, name="cart"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("search", views.search, name= "search"),

    path("update_item", views.updateItem, name="update_item"),
]