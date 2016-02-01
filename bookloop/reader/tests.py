from django.test import TestCase
from reader.models import *
from reader.models import Book
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your tests here.
class ModelTests(TestCase):
    def test_book(self):
        b1 = Book.objects.create(name='b1', isbn='RENNOC-IS-HERE', authors='Bob', pub_date=datetime.date(2016, 1, 1))
        b1.save()

        self.assertEqual(b1.name, 'b1')
        self.assertEqual(b1.isbn, 'RENNOC-IS-HERE')
        self.assertEqual(b1.authors, 'Bob')
        self.assertEqual(str(b1.pub_date), '2016-01-01')

    def test_recommendation(self):
        b1 = Book.objects.create(name='b1', isbn='RENNOC-IS-HERE', authors='Bob', pub_date=datetime.date(2016, 1, 1))
        b1.save()
        recommend = Recommendation.objects.create(book=b1, comment='abcdefghijklmnopqrstuvwxyz ', date=datetime.date(2016, 1, 1))
        recommend.save()

        self.assertEqual(recommend.comment, 'abcdefghijklmnopqrstuvwxyz ')
        self.assertEqual(str(recommend.date), '2016-01-01')

    def test_recommendship(self):
        b1 = Book.objects.create(name='b1', isbn='RENNOC-IS-HERE', authors='Bob', pub_date=datetime.date(2016, 1, 1))
        b1.save()
        comment = 'abcdefghijklmnopqrstuvwxyznowinomyABCnexttimewillusinwithme'
        today = datetime.date.today()
        user = User.objects.create_user('john', 'john@example.com', 'johnpassword')
        recommendation = Recommendation.objects.create(book=b1, comment=comment, date=today)
        recommendship = RecommendShip.objects.create(recommendation=recommendation, to_users=user, from_user=user)

        user.save()
        recommendation.save()
        recommendship.save()

        self.assertEqual(recommendship.recommendation.comment, comment)
        self.assertEqual(recommendship.recommendation.date, today)
        self.assertEqual(recommendship.to_users, user)
        self.assertEqual(recommendship.from_user, user)

    def test_to_users_books(self):
        b1 = Book.objects.create(name='b1', isbn='RENNOC-IS-HERE', authors='Bob', pub_date=datetime.date(2016, 1, 1))
        b1.save()
        b2 = Book.objects.create(name='b2', isbn='RENNOC-IS-HERE', authors='Bob', pub_date=datetime.date(2016, 1, 1))
        b2.save()
        r1 = Recommendation.objects.create(book=b1, comment='abcdefghijklmnopqrstuvwxyz ', date=datetime.date(2016, 1, 1))
        r1.save()
        r2 = Recommendation.objects.create(book=b2, comment='abcdefghijklmnopqrstuvwxyz ', date=datetime.date(2016, 1, 2))
        r2.save()

        u1 = User.objects.create_user('u1', 'u1@example.com', 'u1password')
        u1.save()
        u2 = User.objects.create_user('u2', 'u2@example.com', 'u2password')
        u2.save()
        rs1 = RecommendShip(recommendation=r1, to_users=u2, from_user=u1)
        rs1.save()
        rs2 = RecommendShip(recommendation=r2, to_users=u2, from_user=u1)
        rs2.save()

        for rs in RecommendShip.objects.filter(to_users=u2):
            self.assertEqual(rs, rs1) if rs == rs1 else self.assertEqual(rs, rs2)
            self.assertEqual(rs.recommendation.book, r1.book) if rs == rs1 else self.assertEqual(rs.recommendation.book, r2.book)
        
    def test_from_user_books(self):
        b1 = Book.objects.create(name='b1', isbn='RENNOC-IS-HERE', authors='Bob', pub_date=datetime.date(2016, 1, 1))
        b1.save()
        b2 = Book.objects.create(name='b2', isbn='RENNOC-IS-HERE', authors='Bob', pub_date=datetime.date(2016, 1, 1))
        b2.save()
        r1 = Recommendation.objects.create(book=b1, comment='abcdefghijklmnopqrstuvwxyz ', date=datetime.date(2016, 1, 1))
        r1.save()
        r2 = Recommendation.objects.create(book=b2, comment='abcdefghijklmnopqrstuvwxyz ', date=datetime.date(2016, 1, 2))
        r2.save()

        u1 = User.objects.create_user('u1', 'u1@example.com', 'u1password')
        u1.save()
        u2 = User.objects.create_user('u2', 'u2@example.com', 'u2password')
        u2.save()
        u3 = User.objects.create_user('u3', 'u3@example.com', 'u3password')
        u3.save()
        rs1 = RecommendShip(recommendation=r1, to_users=u2, from_user=u1)
        rs1.save()
        rs2 = RecommendShip(recommendation=r2, to_users=u2, from_user=u1)
        rs2.save()
        rs3 = RecommendShip(recommendation=r1, to_users=u3, from_user=u1)
        rs3.save()

        books = set()
        for rs in RecommendShip.objects.filter(from_user=u1):
            books.add(rs.recommendation.book)
        self.assertEqual(books, set([b1, b2]))

    def test_popular_books(self):
        b1 = Book.objects.create(name='b1', isbn='RENNOC-IS-HERE', authors='Bob', pub_date=datetime.date(2016, 1, 1))
        b1.save()
        b2 = Book.objects.create(name='b2', isbn='RENNOC-IS-HERE', authors='Bob', pub_date=datetime.date(2016, 1, 1))
        b2.save()
        r1 = Recommendation.objects.create(book=b1, comment='abcdefghijklmnopqrstuvwxyz ', date=datetime.date(2016, 1, 1))
        r1.save()
        r2 = Recommendation.objects.create(book=b2, comment='abcdefghijklmnopqrstuvwxyz ', date=datetime.date(2016, 1, 2))
        r2.save()

        u1 = User.objects.create_user('u1', 'u1@example.com', 'u1password')
        u1.save()
        u2 = User.objects.create_user('u2', 'u2@example.com', 'u2password')
        u2.save()
        u3 = User.objects.create_user('u3', 'u3@example.com', 'u3password')
        u3.save()
        rs1 = RecommendShip(recommendation=r1, to_users=u2, from_user=u1)
        rs1.save()
        rs2 = RecommendShip(recommendation=r2, to_users=u2, from_user=u1)
        rs2.save()
        rs3 = RecommendShip(recommendation=r1, to_users=u3, from_user=u1)
        rs3.save()
    
        books = sorted(Book.objects.all(), key=number_of_recommendation_for_a_book, reverse=True)
        self.assertEqual(books, [b1, b2])

        books = sorted(Book.objects.all(), key=number_of_from_user_for_a_book, reverse=True)
        self.assertEqual(books, [b1, b2])

        books = sorted(Book.objects.all(), key=number_of_to_user_for_a_book, reverse=True)
        self.assertEqual(books, [b1, b2])
