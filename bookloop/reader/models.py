from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import User

# Create your models here.

class Book(models.Model):
    name = models.CharField(name='book name', max_length=100)
    isbn = models.CharField(name='isbn', max_length=100)
    authors = models.CharField(name='authors name', max_length=500)
    pub_date = models.DateField(name='date published')

class Recommandation(models.Model):
    comment = models.TextField(name='comment', max_length=5000)
    date = models.DateField(name='recommand date')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    recipients= models.ManyToManyField(
        User,
        through='RecommandShip',
        through_fields=('recommandation', 'person'),
    )

class RecommandShip(models.Model):
    recommandation = models.ForeignKey(Recommandation)
    to_users = models.ForeignKey(User, on_delete=models.CASCADE)
    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="recommandation initiator",
    )
    
