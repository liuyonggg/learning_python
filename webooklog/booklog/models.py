from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.
@python_2_unicode_compatible  # only if you need to support Python 
class User(models.Model):
    first_name = models.CharField('first name', max_length=200)
    last_name  = models.CharField('last name',  max_length=200)
    email = models.EmailField('email')

    def __str__(self):
        return self.email

@python_2_unicode_compatible  # only if you need to support Python 
class Author(models.Model):
    first_name = models.CharField('first name', max_length=200)
    last_name  = models.CharField('last name',  max_length=200)
    email = models.EmailField('email')

    def __str__(self):
        return self.email

@python_2_unicode_compatible  # only if you need to support Python 
class Book(models.Model):
    name = models.CharField('book name', max_length=200)
    pub_date = models.DateTimeField('date published')
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.name

@python_2_unicode_compatible  # only if you need to support Python 
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateTimeField('date reviewed')
    score = models.IntegerField('review score', default=0)
    comment = models.CharField('comment', max_length=100)

    def __str__(self):
        return str(self.score)
