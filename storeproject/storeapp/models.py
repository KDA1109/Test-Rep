from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField(max_length=350)
    registration_date = models.DateTimeField(auto_now_add=True)




class Product(models.Model):
    product_name = models.CharField(max_length=200)
    description = models.TextField(max_length=350)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_amount = models.PositiveIntegerField()
    product_reg_date = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField(upload_to='products/', default=None)





class Order(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    product_id = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, default='processing')

