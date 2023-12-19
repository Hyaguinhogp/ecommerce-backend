from django.db import models

import uuid


class Brands(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        self.name
        
        
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        self.name


class Products(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    price = models.FloatField()
    brand = models.ForeignKey(Brands, related_name='brands', default='', on_delete=models.CASCADE)
    
    def __str__(self):
        self.name