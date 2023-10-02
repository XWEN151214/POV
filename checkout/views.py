from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import CheckoutForm
from .models import CartItem

def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            cart_items = form.cleaned_data['cart_items']

            # Send email to shop admin

            # subject = f'New Order from {name}'
            # message = f'User Name: {name}\nEmail: {email}\nAddress: {address}\n\nCart Details:\n'
            # for item in cart_items:
            #     message += f'{item.product_name} - {item.quantity}\n'
            # send_mail(subject, message, 'admin@example.com', ['admin@example.com'])

            return render(request, 'success.html')
    else:
        form = CheckoutForm()
    return render(request, 'checkout/checkout.html', {'form': form})

