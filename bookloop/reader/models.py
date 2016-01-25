from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
@python_2_unicode_compatible  # only if you need to support Python
class Book(models.Model):
    name = models.CharField('book name', max_length=100)
    isbn = models.CharField('isbn', max_length=100)
    authors = models.CharField('authors name', max_length=100)
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.name

@python_2_unicode_compatible  # only if you need to support Python
class Recommendation(models.Model):
    comment = models.TextField('comment', max_length=5000)
    date = models.DateField('recommend date')
    recipients= models.ManyToManyField(
        User,
        through='RecommendShip',
        through_fields=('recommendation', 'to_users'),
    )

    def __str__(self):
        return self.comment[:25]

@python_2_unicode_compatible  # only if you need to support Python
class RecommendShip(models.Model):
    recommendation = models.ForeignKey(Recommendation)
    to_users = models.ForeignKey(User, on_delete=models.CASCADE)
    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="recommendation initiator+",
    )
    def __str__(self):
        return self.to_users
