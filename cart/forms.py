from django import forms
from .models import Cart

class CartForm(forms.ModelForm):

    quantity = forms.IntegerField()
    product = forms.CharField(widget=forms.Textarea())

    class Meta:

        model = Cart
        fields = [
                  'quantity',
                  'product'
                 ]
        

class CheckoutForm(forms.Form):

    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    address = forms.CharField(max_length=255)
    cart_items = forms.CharField(widget=forms.Textarea())