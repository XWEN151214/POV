from django.shortcuts import (render, redirect, get_object_or_404)
from django.views.generic import (DetailView, View)
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Cart
from .forms import CheckoutForm
from POV.settings import EMAIL_HOST_USER

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
    

class CheckoutView(View):
        
    def post(self, request, *args, **kwargs):

        form = CheckoutForm(request.POST or None)
        if form.is_valid():
            cart = self.get_cart(request)
            context = self.get_context(request, cart)
            html = render_to_string(
                                        'forms/checkout.html',
                                        context=context
                                   )
            send_mail(
                        subject='Checkout Form Submission',
                        message='Cart',
                        from_email=request.user.email,
                        recipient_list=[EMAIL_HOST_USER],
                        html_message=html
                     )
            return redirect(request.META.get('HTTP_REFERER', '/'))

    def get_cart(self, request):

        user = request.user
        return get_object_or_404(Cart, user=user)
    
    def get_context(self, request, cart):

        context = {
                    'user': cart.user,
                    'quantity': cart.quantity,
                    'products': []
                  }
        quantity = request.META.get('QUERY_STRING').split(',')
        counter = 0
        for product in cart.products.all():

            context['products'].append(f'{product.title}: quantity({quantity[counter]})')
            counter += 1
        return context




