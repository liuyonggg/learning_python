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
        recommend = Recommendation.objects.create(comment='abcdefghijklmnopqrstuvwxyz ', date=datetime.date(2016, 1, 1))
        recommend.save()

        self.assertEqual(recommend.comment, 'abcdefghijklmnopqrstuvwxyz ')
        self.assertEqual(str(recommend.date), '2016-01-01')

    def test_recommendship(self):
        comment = 'abcdefghijklmnopqrstuvwxyznowinomyABCnexttimewillusinwithme'
        today = datetime.date.today()
        user = User.objects.create_user('john', 'john@example.com', 'johnpassword')
        recommendation = Recommendation.objects.create(comment=comment, date=today)
        recommendship = RecommendShip.objects.create(recommendation=recommendation, to_users=user, from_user=user)

        user.save()
        recommendation.save()
        recommendship.save()

        self.assertEqual(recommendship.recommendation.comment, comment)
        self.assertEqual(recommendship.recommendation.date, today)
        self.assertEqual(recommendship.to_users, user)
        self.assertEqual(recommendship.from_user, user)


class Question(models.Model):
    text = models.TextField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        order_with_respect_to = 'question'

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.__str__()

class ModelDummyTests(TestCase):

    def setUp(self):
        questions = ["A. how are you doing", "C what day is today", "B what's happending"]
        for q in questions:
            q1 = Question(text=q)
            q1.save()

        answers = ["good", "soso", "bad"]
        for q in questions:
            for a in answers:
                q1 = Question(text=q)
                q1.save()
                a1 = Answer(question=q1, text="%s_%s"%(q, a))
                a1.save()

        self.ordered_answers = []
        questions = ["A. how are you doing", "C what day is today", "B what's happending"]
        answers = ["good", "soso", "bad"]
        for q in questions:
            for a in answers:
                self.ordered_answers.append(Answer.objects.get(text="%s_%s" %(q, a)))

    def test_create_questions(self):
        q = "what time is it"
        q1 = Question(text=q)
        q1.save()
        q1 = Question.objects.get(text=q)
        self.assertEqual(q1.text, q)

        q = "what time is it2"
        q1 = Question.objects.create()
        q1.text = q
        q1.save()
        q1 = Question.objects.get(text=q)
        self.assertEqual(q1.text, q)

        q = "what time is it3"
        q1 = Question.objects.create()
        q1.text = q
        q1.save()
        q1 = Question.objects.get(text=q)
        self.assertEqual(q1.text, q)

    def test_delete_questions(self):
        q = "what time is it4"
        q1 = Question(text=q)
        q1.save()
        q1 = Question.objects.get(text=q)
        self.assertEqual(q1.text, q)
        q1.delete()
        q1 = None
        try:
            q1 = Question.objects.get(text=q)
        except:
            q1 = None
        self.assertFalse(q1)

    def test_ordering_questions(self):
        i = 0
        for a in Answer.objects.all():
            b = self.ordered_answers[i]
            i += 1
            self.assertEqual(a, b)
