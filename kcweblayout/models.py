from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Part(models.Model):
    part_name = models.CharField(max_length=50, default='Learning to Program')
    part_num = models.IntegerField()

class Chapter(models.Model):
    chapter = models.ForeignKey(Part, on_delete=models.CASCADE)
    chap_name = models.CharField(max_length=50)
    chap_num = models.IntegerField(unique=True, serialize=True)

    #def __str__(self):
     #   return "Chapter " + self.chap_num + ": " + self.chap_name