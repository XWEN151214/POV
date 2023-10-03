from django import forms
from django.core.mail import send_mail
from django.conf import settings

class CheckoutForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    address = forms.CharField(max_length=255)
    cart_items = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        address = self.cleaned_data['address']
        cart_items = self.cleaned_data['cart_items']

        cart_items_list = cart_items.split('\n')
        # Send email to shop admin

        subject = f'New Order from {name}'
        sender = email
        recipient = [settings.DEFAULT_FROM_EMAIL]
        message = f'User Name: {name}\nEmail: {email}\nAddress: {address}\n\nCart Details:\n'
        for item in cart_items_list:
            message += f'{item}\n'

        send_mail(subject, message, sender, recipient)
