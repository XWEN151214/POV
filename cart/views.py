from django.shortcuts import render
from .forms import CartForm

# Create your views here.

def cart(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            cartObj= form.save(commit=False)
            cartObj.user_id = request.user
            cartObj.save()
            return render(request,'success.html')
    else:
        form = CartForm()
    return render(request, 'cart.html', {'form': form})
