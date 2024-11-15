from django.db import models

# Create your models here.

class Stud(models.Model):
    naam = models.CharField(max_length=25)
    persent = models.IntegerField()

    def __str__(self):
        return self.naam