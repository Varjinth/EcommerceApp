from django.db import models
from django.contrib.auth.models import User
from myapps.models import Product

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date_added = models.DateTimeField(auto_now_add=True)

    def calculate_subtotal(self):
        self.subtotal = self.quantity * self.price
    
    def __str__(self):
        return f"{self.user.username}'s cart item #{self.pk}"
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=6, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=False,default='')
    email = models.EmailField(default='')
    address = models.CharField(max_length=100, null=False, default='')
    city = models.CharField(max_length=100,null=False, default='')
    state = models.CharField(max_length=100,null=False,default='')
    zip_code = models.CharField(max_length=10,null=False,default='')
    phone = models.CharField(max_length=15,null=False,default='')
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'{self.user.username} - {self.created_at}'








