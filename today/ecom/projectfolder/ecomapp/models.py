from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import model_to_dict

class Category(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name

    @property
    def product_list(self):
        return self.products.all().values()



class Product(models.Model):
    category = models.ForeignKey(Category, related_name= "Product", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.FloatField(max_length=20)
    image = models.ImageField()
    date_added = models.DateTimeField(auto_now_add=True)


    def _str_(self):
        return self.name

    @property
    def category_detail(self):

        return model_to_dict(self.category, fields=['name', 'desc'])

