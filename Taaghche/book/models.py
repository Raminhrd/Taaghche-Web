from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name



class Books(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    author = models.CharField(max_length=100)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    score = models.FloatField()
    description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.title



class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    book = models.ForeignKey(to=Books, on_delete=models.CASCADE)