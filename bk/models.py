from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Store(models.Model):
    regis = models.ForeignKey(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=100)
    loc = models.CharField(max_length=100)

    def __str__(self):
        return self.store_name


class Books(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    refid = models.CharField(max_length=200)
    img = models.ImageField()
    bookname = models.CharField(max_length=300)
