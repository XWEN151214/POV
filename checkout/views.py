from django.shortcuts import render
from .forms import CheckoutForm

def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # form.send_email()
            return render(request, 'success.html')
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {'form': form})

