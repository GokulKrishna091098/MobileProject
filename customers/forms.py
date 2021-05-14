from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cart,Orders

class UserregistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username"]


class CartForm(ModelForm):
    class Meta:
        model=Cart
        fields='__all__'
        widgets = {
            'product': forms.Select(attrs={'class': 'text_inp', 'placeholder': 'Product'}),
            'user': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'User'}),
            'quantity': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'Quantity'}),
        }

class OrderForm(ModelForm):
    class Meta:
        model=Orders
        fields=['address','product','user']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'Address'}),
            'product': forms.Select(attrs={'class': 'text_inp', 'placeholder': 'Product'}),
            'user': forms.TextInput(attrs={'class': 'text_inp', 'placeholder': 'User'})


        }

