from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    """
    Override the UserCreationForm to allow email's.
    """
    email = forms.EmailField(required=True)

    class Meta:
        """
        Fields we want from the User model, and in what order
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']
