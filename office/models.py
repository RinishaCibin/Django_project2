from django.db import models

# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=100)
    hod=models.CharField(max_length=100)
    dept_room=models.CharField(max_length=30)
