from django.db import models
from Ecommerce_app.models import product
# Create your models here.

class Wishlist(models.Model):
    wish_id=models.CharField(max_length=250,blank=True)
    date=models.DateField(auto_now_add=True)

    class Meta:
        db_table='Wishlist'
        ordering=['date']
    def __str__(self):
        return '{}'.format(self.wish_id)
class Wish_item(models.Model):
    products=models.ForeignKey(product,on_delete=models.CASCADE)
    wish=models.ForeignKey(Wishlist,on_delete=models.CASCADE)
    active=models.BooleanField(default=True)
    class Meta:
        db_table='Wish_item'
    def __str__(self):
        return '{}'.format(self.products)