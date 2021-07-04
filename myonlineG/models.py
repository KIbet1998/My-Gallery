from django.db import models
from django.db.models.base import Model

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=100,blank=True,null=True )

    def _str_(self):
        return self.category_name