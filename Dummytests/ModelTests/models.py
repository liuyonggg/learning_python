from __future__ import unicode_literals

from django.db import models

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

class Person(models.Model):
    SHIRT_SIZES = (
        ('XXXS', 'Really???'),
        ('XXS', "C'mon, you can't that small... Fine, Extra Extra Small"),
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', "C'mon, you can't that large... Fine, Extra Extra Large"),
        ('XXXL', 'Really???'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=4, choices=SHIRT_SIZES)

class Manufacturer(models.Model):
    name = models.TextField()

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model = models.TextField()

class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = (['headline'])

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)
