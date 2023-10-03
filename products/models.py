from django.db import models
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
        
class Product(models.Model):
    title    = models.CharField(max_length=100)
    category = models.ForeignKey(Category , on_delete=models.SET_NULL, null=True)
    price    = models.DecimalField(max_digits=10, decimal_places=2)
    instock_Qty = models.IntegerField() 
    description = models.TextField()
    custom      = models.BooleanField(default=False)
    
    def __str__(self): # return name
        return self.title

