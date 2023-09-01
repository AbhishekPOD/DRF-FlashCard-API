
from django.db import models

class Card(models.Model):
    front = models.CharField(max_length=30)
    back = models.CharField(max_length=30)
    source_language = models.CharField(max_length=30)
    target_language = models.CharField(max_length=30)
    difficulty = models.IntegerField()

    def __str__(self):
        return "Card Front Content : " + self.front
