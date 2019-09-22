from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model):

    title  = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    body   = models.TextField()
    ISBN   = models.CharField(max_length=13)

    def __str__(self):

        return self.title

    def get_absolute_url(self):

        return reverse('book_detail', args=[str(self.id)])