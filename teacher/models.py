from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    age = models.IntegerField()
    batch=models.CharField(max_length=50)
    place=models.CharField(max_length=100)

class HomeWork(models.Model):
    subject=models.CharField(max_length=100)
    question=models.CharField(max_length=300)
    submit_date=models.DateField()


