from django.db import models
from django.urls import reverse

# Create your models here.

class Dictionary(models.Model):
    name= models.CharField(max_length=100, unique=True)
    description= models.TextField()
    url= models.URLField(blank=True)
    # icon= pass
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('figures:tables')


class Figures(models.Model):
    name= models.CharField(max_length=100, unique=True)
    description= models.TextField()
    url= models.URLField(blank=True)
    # icon= pass
    date= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('figures:tables')
