from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Order


class OrderForm(ModelForm):
    """
    basic form class
    """

    class Meta:
        model = Order
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    """
    Override the base form
    """
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']