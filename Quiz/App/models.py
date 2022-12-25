from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    rollNo = models.IntegerField()
    standard = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = " Students"


class Cource(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    cource = models.CharField(max_length=100)

    def __str__(self):
        return str(self.cource)


class Question(models.Model):
    coucre = models.ForeignKey(Cource, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    correctAns = models.CharField(max_length=100)
    A = models.CharField(max_length=100)
    B = models.CharField(max_length=100)
    C = models.CharField(max_length=100, blank=True)
    D = models.CharField(max_length=100, blank=True)
    userAns = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.question)
