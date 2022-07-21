from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Component(models.Model):
    brand = models.CharField(max_length=255)
    part = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.brand, self.part

    def get_absolute_url(self):
        return reverse('components_detail', kwargs={'pk': self.id})

class Case(models.Model):
    brand = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    components = models.ManyToManyField(Component)
    
    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('detail', kwargs={'case_id': self.id})





class Comment(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    case = models.ForeignKey(Case,on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.name)

class Photo(models.Model):
    url = models.CharField(max_length=200)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"Photo for case_id: {self.case_id} @{self.url}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='profile_pics', blank=True)
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.username
