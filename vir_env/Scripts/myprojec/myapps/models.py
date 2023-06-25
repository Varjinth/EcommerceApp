from django.db import models

class Product(models.Model):
    s_no = models.IntegerField()
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    specification = models.TextField()
    description = models.TextField()
    remarks = models.TextField()
    
    def __str__(self):
        return self.product_name

