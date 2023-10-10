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

    email = forms.EmailField(max_length=100)
    address = forms.CharField(max_length=255)
    specific_details = forms.CharField(widget=forms.Textarea(), required=False)