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
    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recommendship_from_user',
    )

    def __str__(self):
        return self.comment[:25]

    def __repr__(self):
        return self.__str__()

@python_2_unicode_compatible
class RecommendShip(models.Model):
    recommendation = models.ForeignKey(Recommendation)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recommendship_to_user')

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
        users.add(x.from_user)
    return len(users)

def number_of_to_user_for_a_book(book):
    users = set()
    for x in Recommendation.objects.filter(book=book):
        for u in list(str(list(RecommendShip.objects.filter(recommendation=x))[0].to_user)):
            users.add(u)
    return len(users)

def book_to_read_for_a_user(user):
    list_of_recommendations = list(RecommendShip.objects.filter(to_user=user))
    book = None
    read_book_list = list(ReadBook.objects.filter(user=user))
    for r in list_of_recommendations:
        book = r.recommendation.book
        if book not in read_book_list:
            break
        book = None
    return book

def friends_for_a_user(user):
    res = []
    fl1 = list(FriendShip.objects.filter(from_user=user))
    fl2 = list(FriendShip.objects.filter(to_user=user))
    for f in fl2:
        fl1.append(f)
    del fl2
    for f in fl1:
        if f.from_user == user:
            res.append(f.to_user)
        else:
            res.append(f.to_user)
    return res

def number_of_readers_for_a_book(book):
    brl = list(ReadBook.objects.filter(book=book))
    return len(brl)

def other_readers_for_a_book(user, book):
    fl = friends_for_a_user(user)
    rbl = ReadBook.objects.filter(book=book)
    utr = []
    res = []

    for rb in rbl:
        res.append(rb.user)
    res.remove(user)

    for u in res:
        if u in fl:
            utr.append(u)

    for u in utr:
        res.remove(u)
    return res

def pending_invitation_for_a_user(user):
    res1 = list(FriendShip.objects.filter(from_user=user, status=1))
    res2 = list(FriendShip.objects.filter(to_user=user, status=1))
    res3 = list(FriendShip.objects.filter(from_user=user, status=2))
    res4 = list(FriendShip.objects.filter(to_user=user, status=2))
    for fs in res1:
        res2.append(fs)

    for fs in res3:
        res2.append(fs)

    for fs in res4:
        res2.append(fs)

    return res2

def friends_for_a_user(user):
    res = []
    fl1 = list(FriendShip.objects.filter(from_user=user))
    fl2 = list(FriendShip.objects.filter(to_user=user))
    for f in fl2:
        fl1.append(f)
    for f in fl1:
        if f.from_user == user:
            res.append(f.to_user)
        else:
            res.append(f.to_user)
    return res

def friend_reader_of_a_book(book, user):
    bfrl = []
    uf = friends_for_a_user(user)
    for f in uf:
        r = ReadBook.objects.filter(user=f, book=book)
        if r:
            bfrl.append(f)
    return bfrl

def worm_score(user):
    res = 0
    res += len(list(ReadBook.objects.filter(user=user)))
    res += len(list(Recommendation.objects.filter(from_user=user)))
    return res
