from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator



class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class AudioBook(models.Model):
    title = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    authors = models.CharField(max_length=50)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE , null=True)
    score = models.FloatField(validators=[MinValueValidator(0,0), MaxValueValidator(5,0)])
    description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.title


class AudioBookOrder(models.Model):
    STATUS_CHOICE =(
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    )
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='pending')

    def __str__(self):
        return f'{self.id} by {self.user.username}'
    

class AudioBookOrderItem(models.Model):
    product = models.ForeignKey(to=AudioBook, on_delete=models.CASCADE)
    order = models.ForeignKey(to=AudioBookOrder, on_delete=models.CASCADE, related_name="items")
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.product.title}'