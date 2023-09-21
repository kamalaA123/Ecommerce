from django.db import models
from Ecommerce_app.models import product
# Create your models here.

class Cart(models.Model):
    cart_id=models.CharField(max_length=250,blank=True)
    date=models.DateField(auto_now_add=True)

    class Meta:
        db_table='Cart'
        ordering=['date']
    def __str__(self):
        return '{}'.format(self.cart_id)
class Cart_item(models.Model):
    products=models.ForeignKey(product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)
    class Meta:
        db_table='Cart_item'
    def sub_total(self):
        return self.products.price * self.quantity
    def __str__(self):
        return '{}'.format(self.products)