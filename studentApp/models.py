from django.db import models

# Create your models here.
class student(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=100)
    per=models.DecimalField(max_digits=5,decimal_places=2)