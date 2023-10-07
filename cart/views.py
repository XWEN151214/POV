from django.shortcuts import (render, redirect, get_object_or_404)
from django.views.generic import (DetailView, View)
from .models import Cart

# Create your views here.

class CartDetailView(DetailView):

    queryset = Cart.objects.all()
    template_name = 'cart/cart_detail.html'

    def get_object(self):

        user = self.request.user
        cart = None
        if user.is_authenticated:
            if Cart.objects.filter(user=user):
                cart = get_object_or_404(Cart, user=user)
                return cart
        return Cart.objects.none()


class CartDeleteView(View):

    def get(self, request, *args, **kwargs):

        user = request.user
        cart = get_object_or_404(Cart, user=user)
        cart.products.clear()
        return redirect(request.META.get('HTTP_REFERER', '/'))

