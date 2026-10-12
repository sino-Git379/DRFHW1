from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField( max_length=50)
    code = models.CharField( max_length=50)

class Author(models.Model):
    name = models.CharField( max_length=50)
    age = models.IntegerField()
    country = models.ForeignKey(Country,on_delete=models.CASCADE)

class Book(models.Model):
    title = models.CharField( max_length=50)
    pages = models.IntegerField()
    price = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    