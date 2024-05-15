from shelve import Shelf
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Kategorie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Regale(models.Model):
    name = models.CharField(max_length=50)
    anz_Fächer = models.IntegerField()
    bes_Fächer = models.IntegerField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Waren(models.Model):
    producer = models.CharField(max_length=200)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    length = models.DecimalField(max_digits=5, decimal_places=2)
    width = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Kategorie, on_delete=models.CASCADE)
    shelf = models.ForeignKey(Regale, on_delete=models.CASCADE)
    story = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ware_bilder/')
