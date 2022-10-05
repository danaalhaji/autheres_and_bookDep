from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 255)
    describtion = models.CharField(max_length=255,default= "No Describtion available for this Book!")
    created_at = models.DateTimeField (auto_now_add = True)
    updated_at = models.DateTimeField (auto_now = True)
# create auther Table
class Author (models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    books = models.ManyToManyField (Book, related_name = "Authers")
    created_at = models.DateTimeField (auto_now_add = True)
    updated_at = models.DateTimeField (auto_now = True)
# Create your models here.
