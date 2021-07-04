from django.db import models
from django.db.models.base import Model

# Create your models here.

class Category(models.Model):
    category=models.CharField(max_length=100,blank=True,null=True )

    def _str_(self):
        return self.category

class Location(models.Model):
    location=models.CharField(max_length=50,blank=False ,null=True)
    

    def _str_(self):
        return self.location


class Image(models.Model):
    image=models.ImageField(null=True,blank=False)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=4000)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    location=models.ForeignKey(Location,on_delete=models.CASCADE,null=True)

    def _str_(self):
        return self.name

