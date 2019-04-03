from django.db import models

# Create your models here.
from django.db import models

class Question(models.Model):
    questionText = models.CharField(max_length=200)
    pubDate = models.DateTimeField('date published')

    def __str__(self):
        return self.questionText

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choiceText = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choiceText

