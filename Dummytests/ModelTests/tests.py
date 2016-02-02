from django.test import TestCase
from ModelTests.models import *

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

    def test_edit_questions(self):
        qt = 'what time is it 5?'
        q1 = Question.objects.create(text=qt)
        q1.save
        qe = Question.objects.get(pk=1)
        qe.text = 'abc'
        qe.save()
        q1 = Question.objects.get(text=qt)
        q1.delete()
        self.assertTrue(Question.objects.get(text='abc'))
        try:
            q1 = Question.objects.get(text=qt)
        except:
            q1 = None
            self.assertFalse(q1)

    def test_id_questions(self):
        qt = 'what time is it 6?'
        q1 = Question(text=qt)
        self.assertFalse(q1.id)
        q1.save()
        self.assertEqual(q1.id, 13)

#    def test_save_question(self):
 #       qt = 'what time is it 7?'
  #      q1 = Question(text=qt)
   #     q1.save()
    #    q1 = Question.objects.get(text=qt)
     #   q1.text = 'dkskfjdkfjfjs'
      #  q1.id = 56
       # q1.save(update_fields=['text'])
        #q2 = Question.objects.get(text='456')
       # self.assertEqual(q2.text, '456')
      #  self.assertFalse(q2.id == 56)



    def test_ordering_questions(self):
        i = 0
        for a in Answer.objects.all():
            b = self.ordered_answers[i]
            i += 1
            self.assertEqual(a, b)

