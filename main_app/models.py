from django.db import models
from django.urls import reverse
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

    def get_absolute_url(self):
        return reverse('detail', kwargs={'case_id': self.id})





class Comment(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    case = models.ForeignKey(Case,on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.name)