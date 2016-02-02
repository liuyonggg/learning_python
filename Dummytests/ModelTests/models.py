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
