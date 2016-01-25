from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible  # only if you need to support Python
class Book(models.Model):
    name = models.CharField('book name', max_length=200)
    isbn = models.CharField('isbn', max_length=200)
    authors = models.CharField('author', max_length=200)
    pub_date = models.DateField('data published')

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.__str__()

@python_2_unicode_compatible  # only if you need to support Python
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateField('date reviewed')
    like = models.SmallIntegerField('like') # +1 like, -1 dislike
    comment = models.CharField('comment', max_length=1000)

    def __str__(self):
        return self.comment

    def __repr__(self):
        return self.__str__()
