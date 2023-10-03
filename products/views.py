from django.shortcuts import render
from .forms import ProductForm
# Create your views here.

def products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'success.html')  
    else:
        form = ProductForm()
    return render(request, 'products.html', {'form': form})
