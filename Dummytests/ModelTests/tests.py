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
#       q1 = Question(text=qt)
 #      q1.save()
 #      q1 = Question.objects.get(text=qt)
   #    q1.text = 'dkskfjdkfjfjs'
    #   q1.id = 56
     #  q1.save(update_fields=['text'])
      # q2 = Question.objects.get(text='456')
      # self.assertEqual(q2.text, '456')
      # self.assertFalse(q2.id == 56)

    def test_foo_display_person(self):
        p = Person.objects.create(name='Bill Cosby', shirt_size='XXXS')
        self.assertEqual(p.name, 'Bill Cosby')
        self.assertEqual(p.shirt_size, 'XXXS')
        self.assertEqual(p.get_shirt_size_display(), 'Really???')

    def test_ordering_questions(self):
        i = 0
        for a in Answer.objects.all():
            b = self.ordered_answers[i]
            i += 1
            self.assertEqual(a, b)


    def test_foreign_key(self):
        manufacturers = ['Toyota', 'Honda', 'Nissan', 'Porsche']
        cars = ['SUV', 'Sedan', 'Sports Car', 'Buggy', 'Truck']
        for i in xrange(len(manufacturers)-1):
            m1 = Manufacturer.objects.create(name=manufacturers[i])
            for j in xrange(len(cars)):
                Car.objects.create(manufacturer=m1 ,model=cars[j])

        for i in xrange(len(manufacturers)-1):
            m = Manufacturer.objects.get(name=manufacturers[i])
            cars_per_manufacturer = Car.objects.filter(manufacturer=m)
            numbers = [0, 1, 2, 3]
            for n in numbers:
                cars_per_manufacturer[n].model
            self.assertEqual(len(cars), len(cars_per_manufacturer))
            n = 0
            j = 0
            while n < len(cars):
                self.assertEqual(cars_per_manufacturer[j].model, cars[n])
                n += 1
                j += 1

    def test_foreign_key_2(self):
        cars = ['SUV', 'Sedan', 'Truck']

        m1 = Manufacturer.objects.create(name='Toyota')
        for i in xrange(len(cars)-1):
            Car.objects.create(manufacturer=m1 ,model=cars[i])

        for i in xrange(len(cars)-1):
            c = Car.objects.get(model=cars[i])
            m = Manufacturer.objects.get(car=c)
            self.assertEqual(m.name, 'Toyota')

    def test_many_to_many(self):
        p1 = Publication(title="Bob's Awesomeness")
        p2 = Publication(title="Bob's Life")
        p3 = Publication(title='Bob Weekly')
        
        p1.save()
        p2.save()
        p3.save()

        a1 = Article(headline="Bob's Net Worth has Surged Above $1 Billion!!!")

        a1.save()
        a1.publications.add(p1, p2, p3)

        self.assertEqual(str(list(a1.publications.all())[0]), 'Bob Weekly')
        self.assertEqual(str(list(a1.publications.all())[1]), "Bob's Awesomeness")
        self.assertEqual(str(list(a1.publications.all())[2]), "Bob's Life")
        self.assertEqual(str(list(p1.article_set.all())[0]), "Bob's Net Worth has Surged Above $1 Billion!!!")
        self.assertEqual(str(list(p2.article_set.all())[0]), "Bob's Net Worth has Surged Above $1 Billion!!!")
        self.assertEqual(str(list(p3.article_set.all())[0]), "Bob's Net Worth has Surged Above $1 Billion!!!")
        self.assertEqual(list(p1.article_set.exclude(headline="Bob's Net Worth has Surged Above $1 Billion!!!")), [])

        a2 = Article(headline='Bob and His Wife Divorced!!!')
        a3 = Article(headline='Bob Started Funding for a New Company!!!')
        a2.save()
        a3.save()
        a2.publications.add(p2)
        a3.publications.add(p3)
        a1.publications.remove(p2, p3)

        self.assertEqual(str(list(Article.objects.filter(publications=p1))), "[<Article: Bob's Net Worth has Surged Above $1 Billion!!!>]")
        self.assertEqual(str(list(Article.objects.filter(publications=p2))), "[<Article: Bob and His Wife Divorced!!!>]")
        self.assertEqual(str(list(Article.objects.filter(publications=p3))), "[<Article: Bob Started Funding for a New Company!!!>]")

        p4 = Publication(title='The Bobby America Magizine')
        p4.save()
        p4.article_set = [a1, a2, a3]
        self.assertEqual(str(list(p4.article_set.all())), "[<Article: Bob Started Funding for a New Company!!!>, <Article: Bob and His Wife Divorced!!!>, <Article: Bob's Net Worth has Surged Above $1 Billion!!!>]")

    def test_one_to_one(self):
        p1 = Place.objects.create(name='TestR1', address='TestA1')
        p2 = Place.objects.create(name='TestR2', address='TestA2')
        p3 = Place.objects.create(name='TestR3', address='TestA3')

        r1 = Restaurant.objects.create(place=p1, serves_hot_dogs=False, serves_pizza=False)
        r2 = Restaurant.objects.create(place=p2, serves_hot_dogs=True, serves_pizza=True)

        w1 = r1.waiter_set.create(name='Bob')
        w2 = r1.waiter_set.create(name='Joe')
        w3 = r1.waiter_set.create(name='Kevin')
        w4 = r1.waiter_set.create(name='Boblina')
        w5 = r2.waiter_set.create(name='William')
        w6 = r2.waiter_set.create(name='Chrie')
        w7 = r2.waiter_set.create(name='Jessica')
        w8 = r2.waiter_set.create(name='Jessie')

        w1.save()
        w2.save()
        w3.save()
        w4.save()
        w5.save()
        w6.save()
        w7.save()
        w8.save()

        self.assertTrue(hasattr(p1, 'restaurant'))
        self.assertTrue(hasattr(p2, 'restaurant'))
        self.assertFalse(hasattr(p3, 'restaurant'))

        self.assertEqual(p1.restaurant, r1)
        self.assertEqual(p2.restaurant, r2)

        self.assertEqual(r1.place, p1)
        self.assertEqual(r2.place, p2)

        self.assertEqual(list(r1.waiter_set.filter(name__startswith ='J')), [w2])
        self.assertEqual(list(r1.waiter_set.filter(name__startswith ='K')), [w3])
        self.assertEqual(list(r1.waiter_set.filter(name__startswith ='B')), [w1, w4])

        self.assertEqual(list(r2.waiter_set.filter(name__endswith ='m')), [w5])
        self.assertEqual(list(r2.waiter_set.filter(name__endswith ='a')), [w7])
        self.assertEqual(list(r2.waiter_set.filter(name__endswith ='e')), [w6, w8])

        self.assertEqual(list(r1.waiter_set.filter(name__contains ='a')), [w4])
        self.assertEqual(list(r2.waiter_set.filter(name__contains ='e')), [w6, w7, w8])
