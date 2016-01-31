from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

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
    book = models.OneToOneField('book')
    date = models.DateField('recommend date', default=timezone.now)
    comment = models.TextField('comment', max_length=5000)
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
    to_users = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recommendship_to_users')
    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recommendship_from_user',
    )
    def __str__(self):
        return self.to_users


def number_of_recommendation_for_a_book(book):
    return len(Recommendation.objects.filter(book=book))

def number_of_from_user_for_a_book(book):
    users = set()
    for x in Recommendation.objects.filter(book=book):
        for y in RecommendShip.objects.filter(recommendation=x):
            users.add(y.from_user)
    return len(users)

def number_of_to_user_for_a_book(book):
    users = set()
    for x in Recommendation.objects.filter(book=book):
        for u in x.recipients.all():
            users.add(u)
    return len(users)


