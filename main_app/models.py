from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Case(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
