from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    USER_TYPE = [
        ("A",'Auther'),
        ("C",'Customer')
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPE)

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()

class Status(models.Model):
    name = models.CharField(max_length=100, default="in stock")


class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="book")
    description = models.TextField()
    price = models.DecimalField(max_length=10, decimal_places=2)
    quantity = models.IntegerField()
    Status = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, default=1)
    published_at = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)










