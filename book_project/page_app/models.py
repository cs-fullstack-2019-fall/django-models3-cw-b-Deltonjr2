# Create your models here.
from django.db import models
from django.utils import timezone


# Create your models here.
# Create a Book model with name, pageNumber, genre, and publishDate attributes. Create 2 entries using 2 different methods (admin site and class construtor using an endpoint).
#
# Create an 'all/' endpoint that prints out all entry names, create a new endpoint that only prints entries with publish dates greater than or equal to 01/01/2018.

# Create a Book model with name, pageNumber, genre, and publishDate attributes.
class Book(models.Model):
    name = models.CharField(max_length=100)
    pageNumber = models.IntegerField()
    Genre = models.CharField(max_length=100)
    publishDate = models.CharField(max_length=100)


    def book_(self):
        return self.book

def __str__(self):
    return self.book
