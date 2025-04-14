from django.db import models

from store.models.customer import Customer
from store.models.product import Product


class Order(models.Model):
   order_date = models.DateTimeField(auto_now_add=True)
   customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='orders')


   def __str__(self):
       return f"Order {self.id} by {self.customer}"


   class Meta:
       ordering = ['-order_date']
       get_latest_by = 'order_date'


class OrderItem(models.Model):
   order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
   product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_items')
   quantity = models.PositiveSmallIntegerField()
   price = models.DecimalField(max_digits=10, decimal_places=2)


   def __str__(self):
       return f"{self.quantity} x {self.product.name} for {self.order}"
