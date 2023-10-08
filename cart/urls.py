from django.urls import path
from .views import (CartDetailView, CartDeleteView,
                    CheckoutView
                   )

app_name = 'cart'

urlpatterns = [
    path('detail', CartDetailView.as_view(), name='detail'),
    path('delete', CartDeleteView.as_view(), name='delete'),
    path('checkout', CheckoutView.as_view(), name='checkout')
]