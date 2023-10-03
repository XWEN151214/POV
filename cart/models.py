from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# decorator prop
class Cart(models.Model): 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product  = models.ManyToManyField(Product)
    quantity = models.IntegerField()  # no_of_prod
    
    @property #cart.total
    def total(self):
        total = 0
        for product in self.product.all():
            total += product.price * self.quantity
        return total
    