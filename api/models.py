from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db import transaction

class User(models.Model):
    username = models.CharField(max_length=69)
    phone = models.CharField(max_length=13)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Telegram User'
        verbose_name_plural = 'Telegram Users'


class Category(models.Model):
    category_name = models.CharField(max_length=100,verbose_name='Maxsulot kategoriyasi')
    
    def __str__(self) -> str:
        return self.category_name
    
class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    name = models.TextField(max_length=100,null=False, blank=False,verbose_name='Maxsulot nomi')
    create_time = models.DateTimeField(verbose_name='Ishlab chiqarilgan vaqti')
    expiry_date = models.DateTimeField(verbose_name='Yaroqlilik muddati')
    quantity = models.PositiveIntegerField()
    price= models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='mediafile/')

    def __str__(self) -> str:
        return self.name

    def clean(self):
        if Product.objects.exclude(id=self.id).filter(name=self.name).exists():
            raise ValidationError("Bu nom bilan maxsulot allaqachon mavjud.")

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    
class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self) -> str:
        return f"{self.customer} --> {str(self.date)}dagi oderi"

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    mount = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0,null=True,blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.product} {self.mount} miqdorda {self.order}"
    
    #tanlangan maxsulotni narxini olib keladi agar maxsulot narxi kiritilmasa o'zi defaultda yozad va producdan olingan maxsulotni quantitydan ayiradi
    def save(self, *args, **kwargs):
        if not self.total_price:
            self.total_price = self.product.price * self.mount

        product_price = self.product.price * self.mount
        if self.total_price != product_price:
            raise ValidationError("Maxsulot narxi noto'g'ri")

        if self.mount > self.product.quantity:
            raise ValidationError("Maxsulotlar miqdori yetarli emas")

        self.product.quantity -= self.mount
        self.product.save()

        super().save(*args, **kwargs)
    

