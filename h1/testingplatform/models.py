from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=250)
    subject = models.CharField(max_length=50)
    subtopic = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)