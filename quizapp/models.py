from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Quizzes(models.Model):
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)


class Question(models.Model):
    quiz = models.ForeignKey(Quizzes, related_name='question', on_delete=models.DO_NOTHING)


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.DO_NOTHING)