from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

FRIEND_STATUS = (
    (1, "Created"),
    (2, "Sent"),
    (3, "Failed"),
    (4, "Expired"),
    (5, "Accepted"),
    (6, "Declined"),
    (7, "Deleted")
)

class FriendShip(models.Model):
    from_user = models.ForeignKey(User, related_name="friendship_from_user")
    to_user = models.ForeignKey(User, related_name="friendship_to_user")
    date = models.DateField('start date', default=timezone.now().date())
    status = models.IntegerField(choices=FRIEND_STATUS)

    def __str__(self):
        return "%s <-> %s" % (self.from_user.username, self.to_user.username)

    def __repr__(self):
        return self.__str__()


@python_2_unicode_compatible
class Book(models.Model):
    name = models.CharField('book name', max_length=100)
    isbn = models.CharField('isbn', max_length=100)
    authors = models.CharField('authors name', max_length=100)
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

@python_2_unicode_compatible
class Recommendation(models.Model):
    book = models.OneToOneField('book')
    date = models.DateField('recommend date', default=timezone.now().date())
    comment = models.TextField('comment', max_length=5000)
    recipients= models.ManyToManyField(
        User,
        through='RecommendShip',
        through_fields=('recommendation', 'to_user'),
    )

    def __str__(self):
        return self.comment[:25]

    def __repr__(self):
        return self.__str__()

@python_2_unicode_compatible
class RecommendShip(models.Model):
    recommendation = models.ForeignKey(Recommendation)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recommendship_to_user')
    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recommendship_from_user',
    )
    def __str__(self):
        return '%s -> %s' %(self.from_user.username, self.to_user.username)

    def __repr__(self):
        return self.__str__()


class ReadBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reader')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='read_book')
    date = models.DateField('finish date', default=timezone.now().date())

    def __str__(self):
        return '%s read  %s on %s' %(self.user, self.book, self.date)

    def __repr__(self):
        return self.__str__()
    
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









#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!         
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!
#You are entering TRASH ZONE!!!


'''
@python_2_unicode_compatible
class User(models.Model):
    auth_user = models.ForeignKey(AuthUser, related_name="user_auth_user")
    friends = models.ManyToManyField('self', 
        related_name='user_friends',
        through='FriendShip',
        through_fields=('from_user', 'to_user'),
        symmetrical=False,
        )

    def __str__(self):
        return self.username
    
    def __repr__(self):
        return self.__str__()

    def number_recommended_books_from_a_friend(self, friend):
        return len(RecommendShip.objects.filter(to_user=self, from_user=friend))
'''
        

