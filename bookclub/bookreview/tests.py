from django.test import TestCase
from bookreview.models import *
import datetime
from django.contrib.auth.models import User

# Create your tests here.

class BookModelTests(TestCase):
    def test_book(self):
        b = Book(name = 'name1', isbn='1234', authors='author1, author2', pub_date=datetime.date(2016, 1, 22))
        self.assertEqual(b.name , 'name1')
        self.assertEqual(b.isbn, '1234')
        self.assertEqual(b.authors , 'author1, author2')
        self.assertEqual(b.pub_date , datetime.date(2016, 1, 22))

    def test_review(self):
        uname = 'john'
        password = 'johnpassword'
        u1 = User.objects.create_user(uname, 'john@example.com', password)
        b = Book(name = 'name1', isbn='1234', authors='author1, author2', pub_date=datetime.date(2015, 1, 22))
        r = Review(user=u1, book=b, date=datetime.date(2016, 1, 22), like=1, comment='good book')
        self.assertEqual(r.user, u1)
        self.assertEqual(r.book, b)
        self.assertEqual(r.date, datetime.date(2016, 1, 22))
        self.assertEqual(r.like, 1)
        self.assertEqual(r.comment, 'good book')
        
