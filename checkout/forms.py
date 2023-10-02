from django import forms
from .models import CartItem

class CheckoutForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    address = forms.CharField(max_length=255)
    cart_items = forms.ModelMultipleChoiceField(
        queryset=CartItem.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
